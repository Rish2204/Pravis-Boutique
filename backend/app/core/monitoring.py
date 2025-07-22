import os
import logging
from typing import Dict, Any, Optional
import json
from datetime import datetime
import requests
import time
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

# Configure Azure Application Insights if enabled
AZURE_APP_INSIGHTS_KEY = os.getenv("AZURE_APP_INSIGHTS_KEY", "")
AZURE_APP_INSIGHTS_ENABLED = bool(AZURE_APP_INSIGHTS_KEY)

# Configure Azure Log Analytics if enabled
AZURE_LOG_ANALYTICS_WORKSPACE_ID = os.getenv("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
AZURE_LOG_ANALYTICS_SHARED_KEY = os.getenv("AZURE_LOG_ANALYTICS_SHARED_KEY", "")
AZURE_LOG_ANALYTICS_ENABLED = bool(AZURE_LOG_ANALYTICS_WORKSPACE_ID and AZURE_LOG_ANALYTICS_SHARED_KEY)

# Configure logger
logger = logging.getLogger("app.monitoring")

class AzureMonitoring:
    """Azure monitoring integration for Application Insights and Log Analytics"""
    
    @staticmethod
    def send_to_app_insights(event_name: str, properties: Dict[str, Any]):
        """Send telemetry data to Azure Application Insights"""
        if not AZURE_APP_INSIGHTS_ENABLED:
            return
        
        try:
            # App Insights REST API endpoint
            url = f"https://dc.services.visualstudio.com/v2/track"
            
            # Prepare the telemetry data
            telemetry_data = {
                "name": event_name,
                "time": datetime.utcnow().isoformat() + "Z",
                "iKey": AZURE_APP_INSIGHTS_KEY,
                "tags": {
                    "ai.cloud.role": "pravis-boutique-api",
                    "ai.cloud.roleInstance": os.getenv("HOSTNAME", "local"),
                    "ai.application.ver": "1.0.0"
                },
                "data": {
                    "baseType": "EventData",
                    "baseData": {
                        "ver": 2,
                        "name": event_name,
                        "properties": properties
                    }
                }
            }
            
            # Send the telemetry data
            response = requests.post(url, json=telemetry_data, timeout=1.0)
            response.raise_for_status()
        except Exception as e:
            logger.error(f"Error sending data to Application Insights: {str(e)}")

    @staticmethod
    def send_to_log_analytics(log_type: str, log_data: Dict[str, Any]):
        """Send logs to Azure Log Analytics workspace"""
        if not AZURE_LOG_ANALYTICS_ENABLED:
            return
        
        try:
            # Build the API signature
            workspace_id = AZURE_LOG_ANALYTICS_WORKSPACE_ID
            shared_key = AZURE_LOG_ANALYTICS_SHARED_KEY
            
            # Prepare the log entry
            log_entry = json.dumps(log_data)
            
            # Build the API URL
            url = f"https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01"
            
            # Build the headers with authentication
            import base64
            import hmac
            import hashlib
            import datetime
            
            # Create the signature
            rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            content_length = len(log_entry)
            signature_string = f"POST\n{content_length}\napplication/json\nx-ms-date:{rfc1123date}\n/api/logs"
            
            # Create the HMAC signature
            signature = base64.b64encode(
                hmac.new(
                    base64.b64decode(shared_key),
                    signature_string.encode('utf-8'),
                    digestmod=hashlib.sha256
                ).digest()
            ).decode('utf-8')
            
            # Create the authorization header
            authorization = f"SharedKey {workspace_id}:{signature}"
            
            # Set the headers
            headers = {
                'content-type': 'application/json',
                'Authorization': authorization,
                'Log-Type': log_type,
                'x-ms-date': rfc1123date
            }
            
            # Send the log data
            response = requests.post(url, data=log_entry, headers=headers, timeout=3.0)
            response.raise_for_status()
        except Exception as e:
            logger.error(f"Error sending logs to Log Analytics: {str(e)}")

    @staticmethod
    def log_api_request(request_id: str, method: str, path: str, status_code: int,
                      duration_ms: float, user_id: Optional[str] = None):
        """Log API request metrics to Azure monitoring"""
        # Prepare the log data
        log_data = {
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat(),
            "method": method,
            "path": path,
            "status_code": status_code,
            "duration_ms": duration_ms,
            "environment": settings.ENVIRONMENT,
            "user_id": user_id,
            "service": "pravis-boutique-api"
        }
        
        # Send to both monitoring services
        AzureMonitoring.send_to_app_insights("APIRequest", log_data)
        AzureMonitoring.send_to_log_analytics("PravisBoutiqueAPI_Requests", log_data)

    @staticmethod
    def log_exception(request_id: str, exception_type: str, exception_message: str, 
                    path: str, method: str, user_id: Optional[str] = None):
        """Log exception to Azure monitoring"""
        # Prepare the log data
        log_data = {
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat(),
            "exception_type": exception_type,
            "exception_message": exception_message,
            "path": path,
            "method": method,
            "environment": settings.ENVIRONMENT,
            "user_id": user_id,
            "service": "pravis-boutique-api"
        }
        
        # Send to both monitoring services
        AzureMonitoring.send_to_app_insights("Exception", log_data)
        AzureMonitoring.send_to_log_analytics("PravisBoutiqueAPI_Exceptions", log_data)

    @staticmethod
    def log_voice_request(request_id: str, service_type: str, duration_ms: float, 
                        success: bool, text_length: int, user_id: Optional[str] = None,
                        cached: bool = False):
        """Log voice API request metrics to Azure monitoring"""
        # Prepare the log data
        log_data = {
            "request_id": request_id,
            "timestamp": datetime.utcnow().isoformat(),
            "service_type": service_type,  # 'transcription', 'tts', 'chat'
            "duration_ms": duration_ms,
            "success": success,
            "text_length": text_length,
            "cached": cached,
            "environment": settings.ENVIRONMENT,
            "user_id": user_id,
            "service": "pravis-boutique-api"
        }
        
        # Send to both monitoring services
        AzureMonitoring.send_to_app_insights("VoiceRequest", log_data)
        AzureMonitoring.send_to_log_analytics("PravisBoutiqueAPI_VoiceRequests", log_data)


class AzureMonitoringMiddleware(BaseHTTPMiddleware):
    """Middleware to log all API requests to Azure monitoring"""
    
    async def dispatch(self, request: Request, call_next):
        # Generate a unique request ID
        request_id = os.urandom(8).hex()
        
        # Attach request ID to request state
        request.state.request_id = request_id
        
        # Get the start time
        start_time = time.time()
        
        try:
            # Process the request
            response = await call_next(request)
            
            # Calculate request duration
            duration_ms = (time.time() - start_time) * 1000
            
            # Extract user ID if present
            user_id = None
            if hasattr(request.state, "user") and request.state.user:
                user_id = str(request.state.user.id)
            
            # Log the request
            AzureMonitoring.log_api_request(
                request_id=request_id,
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                duration_ms=duration_ms,
                user_id=user_id
            )
            
            return response
            
        except Exception as e:
            # Log the exception
            AzureMonitoring.log_exception(
                request_id=request_id,
                exception_type=type(e).__name__,
                exception_message=str(e),
                path=request.url.path,
                method=request.method,
                user_id=None  # We may not have a user at this point
            )
            
            # Re-raise the exception
            raise


def setup_azure_monitoring(app: FastAPI):
    """Setup Azure monitoring middleware and logging for FastAPI app"""
    # Add middleware for request/response monitoring
    app.add_middleware(AzureMonitoringMiddleware)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    
    # Log application startup
    app_startup_data = {
        "event": "application_startup",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": settings.ENVIRONMENT,
        "version": "1.0.0",
        "service": "pravis-boutique-api"
    }
    
    AzureMonitoring.send_to_app_insights("ApplicationStartup", app_startup_data)
    AzureMonitoring.send_to_log_analytics("PravisBoutiqueAPI_System", app_startup_data)
