#!/usr/bin/env python3
"""
Simple HTTP server for Pravis Boutique API
This is a minimal fallback server to test the basic functionality
"""

import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

class PravisAPIHandler(BaseHTTPRequestHandler):
    def _set_cors_headers(self):
        """Set CORS headers to allow frontend requests"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    
    def _send_json_response(self, data, status_code=200):
        """Send JSON response with proper headers"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self._set_cors_headers()
        self.end_headers()
        
        response = json.dumps(data, indent=2)
        self.wfile.write(response.encode())
        
        # Log the request
        logging.info(f"{self.command} {self.path} - {status_code}")
    
    def do_OPTIONS(self):
        """Handle preflight CORS requests"""
        self.send_response(200)
        self._set_cors_headers()
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == '/':
            # Root endpoint
            self._send_json_response({
                "message": "Welcome to Pravis Boutique API",
                "version": "1.0.0",
                "status": "running",
                "docs": "/docs",
                "environment": "development",
                "timestamp": datetime.utcnow().isoformat()
            })
        
        elif path == '/api/v1/health':
            # Health check endpoint
            self._send_json_response({
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat(),
                "uptime": "running"
            })
        
        elif path.startswith('/api/v1/products'):
            # Mock products endpoint
            products = [
                {
                    "id": 1,
                    "name": "Traditional Silk Saree",
                    "price": 15999,
                    "category": "Sarees",
                    "description": "Beautiful handwoven silk saree with traditional patterns",
                    "image": "/images/saree1.jpg",
                    "in_stock": True
                },
                {
                    "id": 2,
                    "name": "Designer Kurti",
                    "price": 2999,
                    "category": "Kurtis",
                    "description": "Elegant designer kurti for modern women",
                    "image": "/images/kurti1.jpg",
                    "in_stock": True
                },
                {
                    "id": 3,
                    "name": "Wedding Lehenga",
                    "price": 45999,
                    "category": "Lehengas",
                    "description": "Stunning wedding lehenga with intricate embroidery",
                    "image": "/images/lehenga1.jpg",
                    "in_stock": False
                }
            ]
            self._send_json_response({
                "products": products,
                "total": len(products),
                "page": 1,
                "per_page": 10
            })
        
        elif path == '/docs':
            # Simple API documentation
            docs = {
                "title": "Pravis Boutique API Documentation",
                "version": "1.0.0",
                "endpoints": {
                    "GET /": "API information and status",
                    "GET /api/v1/health": "Health check",
                    "GET /api/v1/products": "List all products",
                    "GET /docs": "This documentation"
                },
                "note": "This is a minimal test server. Full FastAPI implementation in main.py"
            }
            self._send_json_response(docs)
        
        else:
            # 404 for unknown endpoints
            self._send_json_response({
                "error": "Not Found",
                "message": f"Endpoint {path} not found",
                "available_endpoints": ["/", "/api/v1/health", "/api/v1/products", "/docs"]
            }, 404)
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'
        
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self._send_json_response({
                "error": "Invalid JSON",
                "message": "Request body must be valid JSON"
            }, 400)
            return
        
        if path == '/api/v1/voice/query':
            # Mock voice agent endpoint
            query = data.get('query', '')
            self._send_json_response({
                "query": query,
                "response": f"Thank you for asking: '{query}'. This is a mock response from the voice agent.",
                "timestamp": datetime.utcnow().isoformat(),
                "agent": "Pravi (Test Mode)"
            })
        
        else:
            self._send_json_response({
                "error": "Not Found",
                "message": f"POST endpoint {path} not found"
            }, 404)

def run_server(port=8000):
    """Run the simple HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, PravisAPIHandler)
    
    print(f"🚀 Pravis Boutique Simple API Server starting on port {port}")
    print(f"📝 Server running at: http://localhost:{port}")
    print(f"📚 API Documentation: http://localhost:{port}/docs")
    print(f"💚 Health Check: http://localhost:{port}/api/v1/health")
    print("🛑 Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped by user")
        httpd.server_close()

if __name__ == "__main__":
    # Get port from environment or use default
    port = int(os.getenv('API_PORT', 8000))
    run_server(port)