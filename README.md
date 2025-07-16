MTG Price Scanner
A computer vision-powered web application that identifies Magic: The Gathering cards from photos and provides instant pricing information from multiple sources.

Project Overview
Problem: MTG players and collectors need quick, accurate pricing information when evaluating cards at shops, trades, or garage sales.
Solution: Upload a photo of any MTG card and get instant identification with current market prices from multiple sources.

Frontend: Live Demo (Coming Soon)

Completed Features

 Project Setup & Architecture - FastAPI backend, React frontend
 Basic Image Upload - Drag & drop interface with validation
 Database Models - PostgreSQL schema for cards, users, searches
 API Foundation - RESTful endpoints with CORS configuration

In Progress

 Image Processing Pipeline - Google Cloud Vision API integration
 Card Identification - Text extraction and card name matching

Planned Features

 Pricing Integration - TCGPlayer, eBay, Card Kingdom APIs
 User Authentication - JWT-based auth system


System Architecture
    A[User] --> B[React Frontend]
    B --> C[FastAPI Backend]
    C --> D[PostgreSQL Database]
    C --> E[Google Cloud Vision API]
    C --> F[TCGPlayer API]
    C --> G[eBay API]
    
MVP Scope: Primary Goal
Upload a photo of a Magic: The Gathering card and get instant identification + pricing with:
70%+ accuracy for cards in good condition
<5 second response time for complete identification + pricing
Pricing from 2-3 major sources (TCGPlayer, eBay, Card Kingdom)
Simple, intuitive web interface with drag-and-drop upload

Contact

Developer: Andrew Lyons
Email: andrew.r.lyons99@gmail.com
LinkedIn: https://www.linkedin.com/in/andrew-lyons-892331205/