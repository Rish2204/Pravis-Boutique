# LinkedIn Job Scraping API

This module provides functionality to search for jobs on LinkedIn based on skillsets and other criteria using web scraping techniques.

## Overview

The LinkedIn Job Scraping API allows users to:
- Search for jobs based on skills/technologies
- Filter by location, experience level, and job type
- Retrieve detailed job information including descriptions and requirements
- Get structured data from LinkedIn job postings

## API Endpoints

### POST `/api/v1/linkedin/search`

Search for jobs on LinkedIn based on provided criteria.

**Request Body:**
```json
{
  "skills": ["Python", "FastAPI", "Machine Learning"],
  "location": "San Francisco, CA",
  "experience_level": "mid_senior",
  "job_type": "full_time", 
  "company": "Google",
  "limit": 20
}
```

**Request Parameters:**
- `skills` (required): List of 1-10 skills to search for
- `location` (optional): Job location (e.g., "San Francisco, CA", "Remote")
- `experience_level` (optional): One of `internship`, `entry_level`, `associate`, `mid_senior`, `director`
- `job_type` (optional): One of `full_time`, `part_time`, `contract`, `temporary`, `volunteer`
- `company` (optional): Specific company name to filter by
- `limit` (optional): Maximum number of jobs to return (1-50, default: 10)

**Response:**
```json
{
  "success": true,
  "total_jobs_found": 15,
  "jobs": [
    {
      "title": "Senior Python Developer",
      "company": "Tech Corp",
      "location": "San Francisco, CA",
      "description": "We are looking for a senior Python developer...",
      "requirements": [
        "5+ years of Python experience",
        "Experience with FastAPI framework"
      ],
      "salary_range": "$120,000 - $180,000",
      "job_type": "full_time",
      "posted_date": "2024-08-14",
      "linkedin_url": "https://www.linkedin.com/jobs/view/123456789",
      "skills_matched": ["Python", "FastAPI"]
    }
  ],
  "search_query": {
    "skills": ["Python", "FastAPI"],
    "location": "San Francisco, CA",
    "experience_level": "mid_senior",
    "job_type": "full_time",
    "limit": 10
  },
  "message": "Successfully found 15 job listings"
}
```

### GET `/api/v1/linkedin/status`

Get the current status of the LinkedIn scraping service.

**Response:**
```json
{
  "status": "ready",
  "jobs_scraped": 0,
  "errors": [],
  "timestamp": "2024-08-14T10:30:00"
}
```

### GET `/api/v1/linkedin/help`

Get detailed help information about using the LinkedIn job scraping API.

## Usage Examples

### Python Example
```python
import requests

# Search for Python jobs
response = requests.post("http://localhost:8000/api/v1/linkedin/search", json={
    "skills": ["Python", "Django", "PostgreSQL"],
    "location": "Remote",
    "experience_level": "mid_senior",
    "job_type": "full_time",
    "limit": 15
})

jobs = response.json()
for job in jobs["jobs"]:
    print(f"{job['title']} at {job['company']} - {job['location']}")
```

### cURL Example
```bash
curl -X POST "http://localhost:8000/api/v1/linkedin/search" \
  -H "Content-Type: application/json" \
  -d '{
    "skills": ["JavaScript", "React", "Node.js"],
    "location": "New York, NY",
    "experience_level": "entry_level",
    "limit": 10
  }'
```

### JavaScript/Fetch Example
```javascript
const searchJobs = async () => {
  const response = await fetch('/api/v1/linkedin/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      skills: ['React', 'TypeScript', 'GraphQL'],
      location: 'Austin, TX',
      job_type: 'full_time',
      limit: 20
    })
  });
  
  const jobs = await response.json();
  console.log(`Found ${jobs.total_jobs_found} jobs`);
  return jobs;
};
```

## Setup Requirements

### Prerequisites
1. **Chrome Browser**: Required for web scraping
2. **ChromeDriver**: Selenium WebDriver for Chrome
   - Install via `pip install webdriver-manager` (automatic)
   - Or download manually from [ChromeDriver](https://chromedriver.chromium.org/)

### Installation
```bash
# Install required dependencies
pip install selenium beautifulsoup4 fastapi

# Install Chrome (Ubuntu/Debian)
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
apt-get update
apt-get install -y google-chrome-stable
```

### Environment Configuration
Create a `.env` file with optional configuration:
```env
# LinkedIn scraping settings
LINKEDIN_DELAY_BETWEEN_REQUESTS=2
LINKEDIN_REQUEST_TIMEOUT=10
LINKEDIN_MAX_JOBS_PER_REQUEST=50

# Rate limiting
LINKEDIN_RATE_LIMIT_PER_MINUTE=5
```

## Architecture

### Components

1. **Schemas** (`app/schemas/linkedin.py`):
   - `JobSearchRequest`: Input validation and parsing
   - `JobListing`: Individual job data structure
   - `JobSearchResponse`: API response format
   - `ScrapingStatus`: Service status information

2. **Service** (`app/services/linkedin_scraper.py`):
   - `LinkedInJobScraper`: Main scraping logic
   - Web driver management
   - URL building and navigation
   - HTML parsing and data extraction

3. **API Endpoints** (`app/api/api_v1/endpoints/linkedin.py`):
   - RESTful API interface
   - Request validation
   - Error handling
   - Response formatting

### Data Flow
1. User sends POST request with job search criteria
2. API validates input using Pydantic schemas
3. Service builds LinkedIn search URL
4. Chrome WebDriver navigates to LinkedIn
5. BeautifulSoup parses HTML content
6. Job data extracted and structured
7. Response returned to user

## Rate Limiting and Best Practices

### Rate Limiting
- Maximum 5 requests per minute per IP
- Maximum 50 jobs per request
- Built-in delays between requests (2 seconds default)

### Best Practices
1. **Respectful Scraping**:
   - Use reasonable delays between requests
   - Don't overwhelm LinkedIn's servers
   - Respect robots.txt guidelines

2. **Error Handling**:
   - Handle network timeouts gracefully
   - Retry failed requests with exponential backoff
   - Log errors for debugging

3. **Performance**:
   - Cache search results when appropriate
   - Use background tasks for large searches
   - Implement proper connection pooling

## Limitations and Considerations

### Technical Limitations
1. **Anti-Bot Measures**: LinkedIn implements various anti-scraping measures
2. **Rate Limiting**: Excessive requests may result in temporary blocking
3. **Content Changes**: LinkedIn may change their HTML structure
4. **Geographic Restrictions**: Some content may be region-specific

### Legal Considerations
1. **Terms of Service**: Review LinkedIn's Terms of Service
2. **Data Usage**: Only use scraped data for legitimate purposes
3. **Privacy**: Respect user privacy and data protection laws
4. **Commercial Use**: Consider licensing requirements for commercial use

### Reliability
- Web scraping is inherently fragile due to website changes
- Implement proper error handling and fallback mechanisms
- Monitor for changes in LinkedIn's structure
- Consider using official APIs when available

## Error Handling

### Common Errors
```json
{
  "success": false,
  "total_jobs_found": 0,
  "jobs": [],
  "search_query": {...},
  "message": "Failed to load job listings - LinkedIn may be blocking requests"
}
```

### Error Types
1. **WebDriver Errors**: Chrome/ChromeDriver issues
2. **Network Timeouts**: Slow or failed page loads
3. **Parsing Errors**: HTML structure changes
4. **Rate Limiting**: Too many requests
5. **Validation Errors**: Invalid input parameters

## Testing

### Unit Tests
```bash
# Run tests
pytest tests/test_linkedin.py -v

# Run with coverage
pytest tests/test_linkedin.py --cov=app.services.linkedin_scraper
```

### Integration Testing
Note: Integration tests require Chrome WebDriver setup and are skipped by default.

```bash
# Run integration tests (requires setup)
pytest tests/test_linkedin.py::TestLinkedInScraperIntegration -v --run-integration
```

## Development

### Local Development
```bash
# Start the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Access interactive API docs
open http://localhost:8000/docs
```

### Adding New Features
1. Update schemas in `app/schemas/linkedin.py`
2. Modify scraper logic in `app/services/linkedin_scraper.py`
3. Add/update API endpoints in `app/api/api_v1/endpoints/linkedin.py`
4. Write tests in `tests/test_linkedin.py`
5. Update documentation

## Monitoring and Logging

### Logging
The service logs various events:
- Search requests and parameters
- Scraping progress and results
- Errors and warnings
- Performance metrics

### Monitoring
Monitor these metrics:
- Request success/failure rates
- Response times
- Error types and frequencies
- Rate limiting incidents

Example log output:
```
2024-08-14 10:30:00 - INFO - Starting LinkedIn job search for skills: ['Python', 'FastAPI']
2024-08-14 10:30:02 - INFO - Searching with URL: https://www.linkedin.com/jobs/search?...
2024-08-14 10:30:05 - INFO - Found 25 job containers
2024-08-14 10:30:08 - INFO - Successfully scraped 10 jobs
```

## Future Enhancements

### Planned Features
1. **Async Processing**: Background job processing for large searches
2. **Caching**: Redis-based caching for frequent searches
3. **API Authentication**: Rate limiting per API key
4. **Data Enrichment**: Additional job details and company information
5. **Export Options**: CSV, PDF export of job listings
6. **Email Alerts**: Notifications for new matching jobs

### Potential Integrations
1. **Database Storage**: Persistent job storage and history
2. **Machine Learning**: Job recommendation engine
3. **Third-party APIs**: Indeed, Glassdoor integration
4. **Notification Services**: Slack, email, SMS alerts