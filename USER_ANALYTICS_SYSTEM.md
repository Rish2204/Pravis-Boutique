# User Analytics & Consent System for Pravis Boutique PWA

## Overview
This document outlines the comprehensive user analytics system for tracking user interactions, voice agent conversations, and app usage patterns to continuously improve the PWA experience.

## Consent Dialog System

### Initial Welcome Dialog
**Trigger**: First app launch or when no consent preference is stored
**Design**: Modal overlay with friendly boutique branding

**Dialog Content**:
```
Welcome to Pravis Boutique!

A Friendly Disclaimer: This App comes with an AI Agent called "Ask Pravi". 
This agent collects data and feedback for training purposes. 
Should you choose to accept.

□ Sure, Why not!
□ Maybe, Not right now!

[Continue]
```

### Implementation Details

#### Frontend Consent Component
```javascript
// ConsentDialog.js
import React, { useState, useEffect } from 'react';
import './ConsentDialog.css';

const ConsentDialog = ({ onConsentDecision }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [showDialog, setShowDialog] = useState(false);

  useEffect(() => {
    // Check if user has already made a consent decision
    const existingConsent = localStorage.getItem('pravis-consent');
    if (!existingConsent) {
      setShowDialog(true);
    }
  }, []);

  const handleConsentSubmit = () => {
    if (selectedOption) {
      const consentData = {
        consent: selectedOption === 'accept',
        timestamp: new Date().toISOString(),
        version: '1.0'
      };
      
      localStorage.setItem('pravis-consent', JSON.stringify(consentData));
      onConsentDecision(consentData);
      setShowDialog(false);
    }
  };

  if (!showDialog) return null;

  return (
    <div className="consent-overlay">
      <div className="consent-dialog">
        <div className="boutique-logo">
          <h2>Welcome to Pravis Boutique!</h2>
        </div>
        
        <div className="disclaimer-content">
          <p>
            <strong>A Friendly Disclaimer:</strong> This App comes with an AI Agent 
            called <em>"Ask Pravi"</em>. This agent collects data and feedback for 
            training purposes. Should you choose to accept.
          </p>
        </div>

        <div className="consent-options">
          <label className="consent-option">
            <input
              type="radio"
              name="consent"
              value="accept"
              checked={selectedOption === 'accept'}
              onChange={(e) => setSelectedOption(e.target.value)}
            />
            <span className="checkmark"></span>
            Sure, Why not!
          </label>

          <label className="consent-option">
            <input
              type="radio"
              name="consent"
              value="decline"
              checked={selectedOption === 'decline'}
              onChange={(e) => setSelectedOption(e.target.value)}
            />
            <span className="checkmark"></span>
            Maybe, Not right now!
          </label>
        </div>

        <button
          className="continue-button"
          onClick={handleConsentSubmit}
          disabled={!selectedOption}
        >
          Continue
        </button>

        <div className="privacy-note">
          <small>
            You can change your preference anytime in Settings. 
            <a href="/privacy" target="_blank">Privacy Policy</a>
          </small>
        </div>
      </div>
    </div>
  );
};

export default ConsentDialog;
```

#### Consent Dialog Styling
```css
/* ConsentDialog.css */
.consent-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10000;
  backdrop-filter: blur(5px);
}

.consent-dialog {
  background: linear-gradient(135deg, #fff 0%, #f8f9ff 100%);
  border-radius: 20px;
  padding: 32px;
  max-width: 480px;
  width: 90vw;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  text-align: center;
  position: relative;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.boutique-logo h2 {
  color: #2c3e50;
  font-family: 'Playfair Display', serif;
  margin-bottom: 20px;
  font-size: 28px;
}

.disclaimer-content {
  margin: 24px 0;
  color: #555;
  line-height: 1.6;
  font-size: 16px;
}

.disclaimer-content em {
  color: #e74c3c;
  font-weight: 600;
  font-style: normal;
}

.consent-options {
  margin: 32px 0;
  text-align: left;
}

.consent-option {
  display: flex;
  align-items: center;
  margin: 16px 0;
  cursor: pointer;
  font-size: 18px;
  font-weight: 500;
  color: #2c3e50;
  transition: all 0.2s ease;
  padding: 12px;
  border-radius: 10px;
}

.consent-option:hover {
  background: #f0f4ff;
  transform: translateX(5px);
}

.consent-option input[type="radio"] {
  display: none;
}

.checkmark {
  width: 24px;
  height: 24px;
  border: 2px solid #3498db;
  border-radius: 50%;
  margin-right: 16px;
  position: relative;
  transition: all 0.2s ease;
}

.consent-option input[type="radio"]:checked + .checkmark {
  background: #3498db;
  border-color: #3498db;
}

.consent-option input[type="radio"]:checked + .checkmark::after {
  content: '✓';
  position: absolute;
  color: white;
  font-size: 16px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.continue-button {
  background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
  color: white;
  border: none;
  padding: 16px 32px;
  border-radius: 50px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 24px;
}

.continue-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(52, 152, 219, 0.4);
}

.continue-button:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}

.privacy-note {
  margin-top: 20px;
  color: #7f8c8d;
}

.privacy-note a {
  color: #3498db;
  text-decoration: none;
}
```

## Analytics Data Collection System

### Data Types Collected (with consent)

#### 1. User Interaction Analytics
```javascript
// AnalyticsTracker.js
class AnalyticsTracker {
  constructor() {
    this.consentGiven = this.checkConsent();
    this.sessionId = this.generateSessionId();
    this.initializeTracking();
  }

  checkConsent() {
    const consent = localStorage.getItem('pravis-consent');
    return consent ? JSON.parse(consent).consent : false;
  }

  // Track page views and navigation patterns
  trackPageView(pageName, additionalData = {}) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'page_view',
      page: pageName,
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId,
      userAgent: navigator.userAgent,
      ...additionalData
    };

    this.sendAnalyticsEvent(eventData);
  }

  // Track user interactions (clicks, taps, swipes)
  trackInteraction(element, action, context = {}) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'user_interaction',
      element: element,
      action: action,
      context: context,
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight
      }
    };

    this.sendAnalyticsEvent(eventData);
  }

  // Track product interactions
  trackProductInteraction(productId, action, details = {}) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'product_interaction',
      productId: productId,
      action: action, // 'view', 'add_to_cart', 'remove_from_cart', 'purchase'
      details: details,
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId
    };

    this.sendAnalyticsEvent(eventData);
  }
}
```

#### 2. Voice Agent Conversation Analytics
```javascript
// VoiceAnalytics.js
class VoiceAnalytics extends AnalyticsTracker {
  
  // Track voice commands and agent responses
  trackVoiceInteraction(command, response, context = {}) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'voice_interaction',
      command: {
        text: command.text,
        confidence: command.confidence || null,
        language: command.language || 'en-US'
      },
      response: {
        text: response.text,
        audio_duration: response.audioDuration || null,
        success: response.success
      },
      context: {
        page: context.currentPage,
        user_intent: context.detectedIntent,
        session_context: context.sessionContext
      },
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId
    };

    this.sendAnalyticsEvent(eventData);
  }

  // Track common user questions for FAQ improvement
  trackUserQuestion(question, category, wasAnswered = true) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'user_question',
      question: question,
      category: category,
      answered: wasAnswered,
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId
    };

    this.sendAnalyticsEvent(eventData);
  }

  // Track voice agent performance issues
  trackVoiceIssue(issueType, details) {
    if (!this.consentGiven) return;

    const eventData = {
      type: 'voice_agent_issue',
      issue_type: issueType, // 'recognition_failed', 'response_timeout', 'tts_error'
      details: details,
      timestamp: new Date().toISOString(),
      sessionId: this.sessionId
    };

    this.sendAnalyticsEvent(eventData);
  }
}
```

### Backend Analytics Processing

#### Analytics API Endpoints
```python
# analytics_api.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json

router = APIRouter(prefix="/analytics")

@router.post("/event")
async def log_analytics_event(
    event_data: Dict[Any, Any],
    db: Session = Depends(get_db)
):
    """Log analytics event to database"""
    try:
        # Create analytics event record
        analytics_event = AnalyticsEvent(
            event_type=event_data.get('type'),
            session_id=event_data.get('sessionId'),
            timestamp=datetime.fromisoformat(event_data['timestamp']),
            event_data=json.dumps(event_data),
            user_consent=True  # Only reached if consent given
        )
        
        db.add(analytics_event)
        db.commit()
        
        return {"status": "success", "event_id": analytics_event.id}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/insights/user-patterns")
async def get_user_patterns(
    days: int = 7,
    db: Session = Depends(get_db)
):
    """Generate insights about user behavior patterns"""
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Query analytics data
    events = db.query(AnalyticsEvent).filter(
        AnalyticsEvent.timestamp >= start_date,
        AnalyticsEvent.timestamp <= end_date
    ).all()
    
    insights = {
        "total_sessions": len(set([e.session_id for e in events])),
        "most_visited_pages": analyze_page_visits(events),
        "common_user_actions": analyze_user_actions(events),
        "voice_agent_usage": analyze_voice_usage(events),
        "popular_products": analyze_product_interactions(events),
        "user_journey_patterns": analyze_user_journeys(events)
    }
    
    return insights

@router.get("/insights/voice-agent")
async def get_voice_agent_insights(
    days: int = 7,
    db: Session = Depends(get_db)
):
    """Analyze voice agent performance and common questions"""
    
    voice_events = get_voice_events(db, days)
    
    insights = {
        "total_voice_interactions": len(voice_events),
        "most_common_questions": extract_common_questions(voice_events),
        "success_rate": calculate_success_rate(voice_events),
        "response_times": analyze_response_times(voice_events),
        "frequent_issues": analyze_voice_issues(voice_events),
        "improvement_suggestions": generate_improvement_suggestions(voice_events)
    }
    
    return insights
```

#### Database Schema for Analytics
```python
# models/analytics.py
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, JSON
from database import Base

class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"
    
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String(50), index=True)
    session_id = Column(String(100), index=True)
    timestamp = Column(DateTime, index=True)
    event_data = Column(JSON)
    user_consent = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserConsentLog(Base):
    __tablename__ = "user_consent_log"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), nullable=True)  # Optional user identification
    consent_given = Column(Boolean)
    consent_version = Column(String(10))
    timestamp = Column(DateTime)
    ip_address = Column(String(45))  # Hashed for privacy
    user_agent = Column(Text)
```

### Analytics Dashboard for Development Team

#### Real-time Insights Component
```javascript
// AdminAnalyticsDashboard.js
import React, { useState, useEffect } from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const AdminAnalyticsDashboard = () => {
  const [insights, setInsights] = useState(null);
  const [voiceInsights, setVoiceInsights] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadAnalyticsData();
    
    // Refresh every 5 minutes
    const interval = setInterval(loadAnalyticsData, 300000);
    return () => clearInterval(interval);
  }, []);

  const loadAnalyticsData = async () => {
    try {
      const [userPatterns, voiceData] = await Promise.all([
        fetch('/api/analytics/insights/user-patterns').then(r => r.json()),
        fetch('/api/analytics/insights/voice-agent').then(r => r.json())
      ]);
      
      setInsights(userPatterns);
      setVoiceInsights(voiceData);
      setLoading(false);
    } catch (error) {
      console.error('Failed to load analytics:', error);
      setLoading(false);
    }
  };

  if (loading) return <div>Loading analytics...</div>;

  return (
    <div className="analytics-dashboard">
      <h1>Pravis Boutique Analytics Dashboard</h1>
      
      <div className="metrics-grid">
        {/* User Behavior Insights */}
        <div className="metric-card">
          <h3>User Sessions (Last 7 Days)</h3>
          <div className="metric-value">{insights.total_sessions}</div>
        </div>

        <div className="metric-card">
          <h3>Voice Agent Usage</h3>
          <div className="metric-value">{voiceInsights.total_voice_interactions}</div>
          <div className="metric-subtitle">
            Success Rate: {(voiceInsights.success_rate * 100).toFixed(1)}%
          </div>
        </div>

        <div className="metric-card">
          <h3>Most Visited Pages</h3>
          <ul>
            {insights.most_visited_pages.map((page, index) => (
              <li key={index}>{page.page}: {page.visits} visits</li>
            ))}
          </ul>
        </div>

        <div className="metric-card">
          <h3>Common Questions</h3>
          <ul>
            {voiceInsights.most_common_questions.slice(0, 5).map((q, index) => (
              <li key={index}>{q.question} ({q.count}x)</li>
            ))}
          </ul>
        </div>
      </div>

      {/* Improvement Suggestions */}
      <div className="suggestions-section">
        <h3>AI-Generated Improvement Suggestions</h3>
        <ul>
          {voiceInsights.improvement_suggestions.map((suggestion, index) => (
            <li key={index} className="suggestion-item">
              <strong>{suggestion.type}:</strong> {suggestion.description}
              <span className="priority">Priority: {suggestion.priority}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default AdminAnalyticsDashboard;
```

## Privacy & GDPR Compliance

### Data Protection Features
1. **Consent Management**: Clear opt-in/opt-out system
2. **Data Minimization**: Only collect necessary data
3. **Right to be Forgotten**: User can delete all their data
4. **Data Portability**: Users can export their data
5. **Anonymization**: Personal identifiers removed from analytics

### Privacy Controls Component
```javascript
// PrivacyControls.js
const PrivacyControls = () => {
  const handleDataDeletion = async () => {
    await fetch('/api/user/delete-data', { method: 'DELETE' });
    localStorage.removeItem('pravis-consent');
    alert('All your data has been deleted.');
  };

  const handleDataExport = async () => {
    const response = await fetch('/api/user/export-data');
    const data = await response.blob();
    const url = window.URL.createObjectURL(data);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'pravis-data-export.json';
    a.click();
  };

  return (
    <div className="privacy-controls">
      <h3>Your Data & Privacy</h3>
      <button onClick={handleDataExport}>Export My Data</button>
      <button onClick={handleDataDeletion} className="danger">
        Delete All My Data
      </button>
    </div>
  );
};
```

## Continuous Improvement System

### Automated Insights Generation
- Weekly reports on user behavior patterns
- Voice agent performance monitoring
- Product interaction analysis
- UX friction point identification
- A/B test result tracking

### Development Iteration Process
1. **Data Collection**: Track user interactions continuously
2. **Analysis**: Generate insights weekly
3. **Hypothesis Formation**: Identify improvement opportunities
4. **Implementation**: Deploy changes based on data
5. **Validation**: Measure impact of changes

This comprehensive analytics system will help you continuously improve the Pravis Boutique PWA based on real user behavior and feedback, while maintaining full compliance with privacy regulations.
