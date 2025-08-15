from typing import List, Optional
from pydantic import BaseModel, Field, validator


class JobSearchRequest(BaseModel):
    """Request model for LinkedIn job search"""
    skills: List[str] = Field(..., description="List of skills to search for", min_items=1, max_items=10)
    location: Optional[str] = Field(None, description="Job location (e.g., 'San Francisco, CA')")
    experience_level: Optional[str] = Field(None, description="Experience level (internship, entry_level, associate, mid_senior, director)")
    job_type: Optional[str] = Field(None, description="Job type (full_time, part_time, contract, temporary, volunteer)")
    company: Optional[str] = Field(None, description="Specific company name")
    limit: int = Field(default=10, ge=1, le=50, description="Maximum number of jobs to return")

    @validator('skills')
    def validate_skills(cls, v):
        if not v:
            raise ValueError('At least one skill must be provided')
        return [skill.strip() for skill in v if skill.strip()]

    @validator('experience_level')
    def validate_experience_level(cls, v):
        if v and v not in ['internship', 'entry_level', 'associate', 'mid_senior', 'director']:
            raise ValueError('Invalid experience level')
        return v

    @validator('job_type')
    def validate_job_type(cls, v):
        if v and v not in ['full_time', 'part_time', 'contract', 'temporary', 'volunteer']:
            raise ValueError('Invalid job type')
        return v


class JobListing(BaseModel):
    """Model for a single job listing"""
    title: str = Field(..., description="Job title")
    company: str = Field(..., description="Company name")
    location: str = Field(..., description="Job location")
    description: Optional[str] = Field(None, description="Job description")
    requirements: Optional[List[str]] = Field(None, description="Job requirements")
    salary_range: Optional[str] = Field(None, description="Salary range if available")
    job_type: Optional[str] = Field(None, description="Job type (full-time, part-time, etc.)")
    posted_date: Optional[str] = Field(None, description="Date when job was posted")
    linkedin_url: Optional[str] = Field(None, description="LinkedIn job posting URL")
    skills_matched: List[str] = Field(default=[], description="Skills from search that match this job")


class JobSearchResponse(BaseModel):
    """Response model for LinkedIn job search"""
    success: bool = Field(..., description="Whether the search was successful")
    total_jobs_found: int = Field(..., description="Total number of jobs found")
    jobs: List[JobListing] = Field(default=[], description="List of job listings")
    search_query: JobSearchRequest = Field(..., description="Original search parameters")
    message: Optional[str] = Field(None, description="Additional message or error details")


class ScrapingStatus(BaseModel):
    """Model for scraping operation status"""
    status: str = Field(..., description="Status of scraping operation")
    jobs_scraped: int = Field(default=0, description="Number of jobs successfully scraped")
    errors: List[str] = Field(default=[], description="List of errors encountered")
    timestamp: str = Field(..., description="Timestamp of operation")