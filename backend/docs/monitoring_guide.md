# Monitoring and Interaction Logging Guide

## Table of Contents
- [Overview](#overview)
- [User and AI Interaction Logging](#user-and-ai-interaction-logging)
- [Azure Monitoring Integration](#azure-monitoring-integration)
- [Local Development Monitoring](#local-development-monitoring)
- [Log Retention and Security](#log-retention-and-security)
- [Using Logs for Model Training](#using-logs-for-model-training)
- [Troubleshooting](#troubleshooting)

## Overview

This guide describes how Pravis Boutique API handles monitoring and logging of user and AI agent interactions. These logs are crucial for:

1. Troubleshooting issues
2. Understanding usage patterns
3. Collecting data for future AI model training
4. Security auditing
5. Performance monitoring

## User and AI Interaction Logging

### Types of Interactions Logged

The system logs the following user-AI interactions:

1. **Voice API Requests**:
   - Transcription requests
   - Text-to-speech conversions
   - Chat interactions

2. **API Interactions**:
   - Endpoints accessed
   - Authentication events
   - Error states

3. **System Events**:
   - Application startup/shutdown
   - Database migrations
   - Configuration changes

### Log Structure

Each interaction log contains:

```json
{
  "request_id": "unique-request-identifier",
  "timestamp": "2023-07-15T12:34:56.789Z",
  "user_id": "user-identifier-or-anonymous",
  "event_type": "voice_request | api_request | exception | system",
  "details": {
    "endpoint": "/api/v1/voice/tts",
    "method": "POST",
    "status_code": 200,
    "duration_ms": 234,
    "service_type": "tts",
    "text_length": 156,
    "cached": false
  },
  "environment": "production",
  "service": "pravis-boutique-api"
}
```

### Securing Sensitive Information

- All personally identifiable information (PII) is encrypted at rest
- Voice recordings are stored with access controls
- No raw passwords or secrets are ever logged
- User consent is obtained for data collection

## Azure Monitoring Integration

### Application Insights

Application Insights is used for real-time monitoring of:

- Request rates, response times, and failure rates
- Dependency rates, response times, and failure rates
- Exceptions
- Page views and load performance (if applicable to client apps)
- AJAX calls from client-side

Configuration:
```python
# In app/core/monitoring.py
AZURE_APP_INSIGHTS_KEY = os.getenv("AZURE_APP_INSIGHTS_KEY", "")
AZURE_APP_INSIGHTS_ENABLED = bool(AZURE_APP_INSIGHTS_KEY)
```

### Log Analytics

Azure Log Analytics provides:

- Centralized log storage
- Custom queries for analysis
- Alerting on specific conditions
- Integration with Azure Security Center
- Long-term log retention

Configuration:
```python
# In app/core/monitoring.py
AZURE_LOG_ANALYTICS_WORKSPACE_ID = os.getenv("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
AZURE_LOG_ANALYTICS_SHARED_KEY = os.getenv("AZURE_LOG_ANALYTICS_SHARED_KEY", "")
AZURE_LOG_ANALYTICS_ENABLED = bool(AZURE_LOG_ANALYTICS_WORKSPACE_ID and AZURE_LOG_ANALYTICS_SHARED_KEY)
```

### Sample Queries

To find slow API requests in Log Analytics:
```kusto
PravisBoutiqueAPI_Requests
| where duration_ms > 1000
| order by duration_ms desc
| take 100
```

To analyze voice service usage patterns:
```kusto
PravisBoutiqueAPI_VoiceRequests
| summarize count() by service_type, bin(timestamp, 1h)
| render timechart
```

## Local Development Monitoring

For local development, logs are output to:

1. Console (stdout)
2. Local log files

Setup:
```python
# In main.py
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
```

## Log Retention and Security

### Retention Policy

- Standard logs: 30 days
- Security-related logs: 1 year
- Anonymized interaction data for model training: 2 years

### Data Protection

- Logs are encrypted at rest in Azure
- Access is limited to authorized personnel
- PII is minimized and protected according to GDPR and other regulations
- Data is stored in the appropriate geographic region according to legal requirements

### Key Vault Integration

Sensitive information is stored in Azure Key Vault:
- Database credentials
- API keys
- Encryption keys
- SSL certificates

## Using Logs for Model Training

Interaction logs provide valuable data for training AI models:

1. **Data Collection Pipeline**:
   - Raw logs are stored in Azure Log Analytics
   - A daily process extracts relevant interactions
   - PII is removed or anonymized
   - Data is structured for model training

2. **Data Quality Metrics**:
   - Success/failure rate of interactions
   - User corrections to AI output
   - Session abandonment rate
   - Follow-up questions

3. **Preparing Training Datasets**:
   - Logs are converted to training examples
   - Human review for quality assurance
   - Balanced dataset creation
   - Test/validation set separation

## Troubleshooting

### Common Issues

1. **Missing Logs**:
   - Check environment variables are set correctly
   - Verify Azure permissions
   - Check network connectivity

2. **High Latency in Log Delivery**:
   - Batch size might be too large
   - Network issues
   - Azure service outages

3. **Log Volume Too High**:
   - Adjust log levels
   - Implement sampling for high-volume endpoints
   - Review and optimize log message size

### Log Levels

- **ERROR**: Service is unusable, immediate attention required
- **WARNING**: Unexpected behavior, but service still functioning
- **INFO**: Standard operational information
- **DEBUG**: Detailed information for debugging (development only)

### Monitoring Dashboard

Access the monitoring dashboard at:
- Development: [http://localhost:8000/monitoring](http://localhost:8000/monitoring)
- Production: [https://app.powerbi.com/pravis-monitoring](https://app.powerbi.com/pravis-monitoring)
