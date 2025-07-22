# User Feedback and Analytics Guide

## Table of Contents
- [Overview](#overview)
- [Feedback Collection](#feedback-collection)
- [Analytics Implementation](#analytics-implementation)
- [Data Processing Pipeline](#data-processing-pipeline)
- [Privacy and Compliance](#privacy-and-compliance)
- [Feature Iteration Process](#feature-iteration-process)
- [Analytics Dashboards](#analytics-dashboards)
- [Technical Implementation](#technical-implementation)

## Overview

This document outlines how Pravis Boutique API collects, processes, and acts upon user feedback and analytics data. These insights are crucial for continuous improvement of the platform and AI agent interactions.

## Feedback Collection

### In-App Feedback Mechanisms

1. **Rating System**:
   - Simple 1-5 star rating for AI interactions
   - Optional comment field for qualitative feedback
   - Contextual feedback (e.g., "Was this response helpful?")

2. **Feedback API Endpoint**:
   ```python
   @router.post("/feedback", response_model=schemas.FeedbackResponse)
   async def submit_feedback(
       feedback: schemas.FeedbackCreate,
       current_user: User = Depends(get_current_user),
       db: Session = Depends(get_db)
   ):
       """Submit user feedback for an interaction."""
       feedback_data = analytics_repository.create_feedback(
           db=db,
           user_id=current_user["id"],
           interaction_id=feedback.interaction_id,
           rating=feedback.rating,
           comment=feedback.comment,
           context=feedback.context
       )
       return feedback_data
   ```

3. **Periodic Surveys**:
   - Quarterly user experience surveys
   - Feature request collection
   - Targeted surveys for specific user segments

### Passive Feedback Collection

1. **Usage Patterns**:
   - Session duration and frequency
   - Feature engagement rates
   - Abandonment points in user flows
   - Error encounters

2. **Voice Interaction Metrics**:
   - Transcription correction rate
   - Repeated voice commands
   - Voice command success rate

## Analytics Implementation

### Key Metrics to Track

1. **User Engagement**:
   - Daily/Monthly Active Users (DAU/MAU)
   - Session frequency and duration
   - Feature usage distribution
   - User retention rates

2. **AI Performance**:
   - Response accuracy (based on user feedback)
   - Response generation time
   - Conversation completion rate
   - Follow-up question frequency

3. **Technical Performance**:
   - API response times
   - Error rates by endpoint
   - Cache hit/miss ratios
   - Resource utilization

### Schema for Analytics Events

The system logs various analytics events with the following structure:

```python
class AnalyticsEvent(BaseModel):
    """Base schema for analytics events."""
    event_type: str
    timestamp: datetime
    user_id: Optional[str]
    session_id: str
    properties: Dict[str, Any]
    
class UserEvent(AnalyticsEvent):
    """Schema for user-initiated events."""
    event_type: Literal["page_view", "button_click", "feature_use", "error"]
    user_agent: str
    ip_address: Optional[str]
    
class AIInteractionEvent(AnalyticsEvent):
    """Schema for AI interaction events."""
    event_type: Literal["voice_request", "transcription", "tts", "conversation"]
    request_duration_ms: int
    request_size_bytes: int
    response_size_bytes: int
    success: bool
    error_type: Optional[str]
    model_used: str
```

## Data Processing Pipeline

### Real-time Analytics

1. **Event Streaming**:
   - User actions and system events are streamed to Azure Event Hubs
   - Real-time processing with Azure Stream Analytics
   - Anomaly detection for immediate response

2. **Live Dashboards**:
   - Current active users
   - System health metrics
   - Error rate monitoring
   - Key performance indicators

### Batch Processing

1. **Daily Aggregation**:
   - Raw events aggregated into daily summaries
   - User cohort analysis
   - Feature usage reports
   - Performance trend analysis

2. **Data Warehouse Integration**:
   - Long-term storage in Azure Synapse Analytics
   - Integration with business intelligence tools
   - Historical trend analysis
   - Machine learning model training data

## Privacy and Compliance

### Data Protection Measures

1. **Data Minimization**:
   - Collect only necessary data
   - Anonymize data when possible
   - Implement appropriate retention policies

2. **Consent Management**:
   - Clear opt-in process for analytics
   - Granular consent options
   - Easy opt-out mechanism

3. **Compliance Frameworks**:
   - GDPR compliance for EU users
   - CCPA compliance for California users
   - Industry-specific regulations as applicable

### User Data Rights

Implement API endpoints for users to:
- Access their collected data
- Request data deletion
- Export their data
- Modify their consent preferences

```python
@router.get("/user/data", response_model=schemas.UserDataExport)
async def export_user_data(current_user: User = Depends(get_current_user)):
    """Allow users to export all their data."""
    return await user_repository.export_user_data(current_user["id"])

@router.delete("/user/data")
async def delete_user_data(current_user: User = Depends(get_current_user)):
    """Allow users to delete all their data."""
    await user_repository.delete_user_data(current_user["id"])
    return {"status": "success", "message": "All user data has been scheduled for deletion"}
```

## Feature Iteration Process

### Data-Driven Development Cycle

1. **Hypothesis Formation**:
   - Form hypotheses about user needs based on feedback and analytics
   - Define measurable success criteria
   - Prioritize based on impact and effort

2. **Feature Implementation**:
   - Develop with analytics integration from the start
   - Include appropriate instrumentation
   - Set up A/B testing when appropriate

3. **Measurement and Analysis**:
   - Collect data on feature usage
   - Compare against success criteria
   - Identify improvement opportunities

4. **Iteration**:
   - Make data-driven refinements
   - Communicate changes to users
   - Restart the cycle

### A/B Testing Framework

Implementation of A/B testing for new features:

```python
@router.get("/feature/{feature_name}")
async def get_feature_config(
    feature_name: str,
    current_user: User = Depends(get_current_user)
):
    """Get feature configuration based on A/B test assignment."""
    # Determine which test variant to show this user
    variant = await ab_testing_service.get_user_variant(
        user_id=current_user["id"],
        feature_name=feature_name
    )
    
    # Log the exposure event
    await analytics_repository.log_ab_test_exposure(
        user_id=current_user["id"],
        feature_name=feature_name,
        variant=variant
    )
    
    return {"feature": feature_name, "variant": variant}
```

## Analytics Dashboards

### Executive Dashboard

- High-level KPIs
- User growth trends
- Revenue metrics (if applicable)
- System health summary

### Product Development Dashboard

- Feature usage metrics
- User feedback summary
- A/B test results
- Prioritized improvement opportunities

### Technical Operations Dashboard

- System performance metrics
- Error rates and patterns
- Resource utilization
- API endpoint performance

## Technical Implementation

### Analytics Client SDK

A lightweight client SDK for consistent analytics collection:

```javascript
// Frontend client example
class PravisAnalytics {
  constructor(apiKey, userId) {
    this.apiKey = apiKey;
    this.userId = userId;
    this.sessionId = generateUUID();
    this.queue = [];
    this.flushInterval = setInterval(() => this.flush(), 10000);
  }
  
  trackEvent(eventType, properties) {
    const event = {
      event_type: eventType,
      timestamp: new Date().toISOString(),
      user_id: this.userId,
      session_id: this.sessionId,
      properties: properties
    };
    this.queue.push(event);
    
    // Flush immediately if queue gets too large
    if (this.queue.length >= 10) {
      this.flush();
    }
  }
  
  async flush() {
    if (this.queue.length === 0) return;
    
    const events = [...this.queue];
    this.queue = [];
    
    try {
      await fetch('/api/v1/analytics/events', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': this.apiKey
        },
        body: JSON.stringify({ events })
      });
    } catch (error) {
      // On failure, add events back to queue
      this.queue = [...events, ...this.queue];
      console.error('Failed to send analytics events:', error);
    }
  }
}
```

### Analytics API Endpoint

```python
@router.post("/analytics/events")
async def record_analytics_events(
    events: List[schemas.AnalyticsEvent],
    api_key: str = Header(...),
    db: Session = Depends(get_db)
):
    """Record multiple analytics events."""
    # Validate API key
    if not await validate_analytics_api_key(api_key, db):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # Process events
    for event in events:
        await analytics_repository.record_event(db, event)
    
    # For high-volume deployments, consider sending to Event Hub instead
    # await event_hub_client.send_batch(EventData(json.dumps(event)) for event in events)
    
    return {"status": "success", "processed": len(events)}
```

### Feedback Analysis

Automated processing of user feedback:

```python
async def analyze_feedback():
    """Process new feedback entries and extract insights."""
    # Get recent feedback
    feedback_entries = await analytics_repository.get_recent_feedback()
    
    # Process comments with sentiment analysis
    for entry in feedback_entries:
        if entry.comment:
            sentiment = await text_analytics_service.analyze_sentiment(entry.comment)
            await analytics_repository.update_feedback_sentiment(entry.id, sentiment)
    
    # Generate weekly summary report
    summary = await generate_feedback_summary(feedback_entries)
    await notification_service.send_feedback_summary(summary)
```

### Integration with Azure

1. **Azure Application Insights**:
   - Real-time monitoring
   - User behavior analytics
   - Performance tracking

2. **Azure Synapse Analytics**:
   - Data warehousing
   - Advanced analytics
   - Machine learning integration

3. **Power BI**:
   - Interactive dashboards
   - Custom reports
   - Data visualization
