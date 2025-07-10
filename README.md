# Deep Research Agent

A sophisticated multi-agent system that conducts comprehensive research on any topic using web searches and generates detailed reports. The system uses multiple AI agents working together to plan searches, gather information, synthesize findings, and deliver results via email.

## Features

- **Multi-Agent Architecture**: Coordinated system of specialized agents for different research tasks
- **Intelligent Search Planning**: Automatically generates optimal search queries for comprehensive coverage
- **Web Search Integration**: Uses DuckDuckGo for web searches to gather current information
- **Comprehensive Report Generation**: Creates detailed markdown reports (1000+ words)
- **Email Delivery**: Automatically sends formatted HTML reports via email
- **Real-time Progress Tracking**: Live updates on research progress
- **Web Interface**: User-friendly Gradio interface for easy interaction

## Architecture

The system consists of five main components:

### 1. Research Manager (`research_manager.py`)
- Orchestrates the entire research process
- Manages the workflow between different agents
- Provides real-time status updates
- Handles error recovery and task coordination

### 2. Planner Agent (`planner_agent.py`)
- Analyzes research queries to determine optimal search strategies
- Generates 3 targeted web searches per query
- Provides reasoning for each search to ensure comprehensive coverage

### 3. Search Agent (`search_agent.py`)
- Executes web searches using DuckDuckGo
- Summarizes search results into concise 2-3 paragraph summaries
- Filters out irrelevant information and focuses on key findings
- Outputs results in structured markdown format

### 4. Writer Agent (`writer_agent.py`)
- Synthesizes all search results into a comprehensive report
- Creates structured outlines and detailed analysis
- Generates 5-10 page reports with 1000+ words
- Provides follow-up questions for further research

### 5. Email Agent (`email_agent.py`)
- Converts markdown reports to formatted HTML emails
- Sends reports via SendGrid API
- Handles email delivery and error management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Deep_Research_Agent
```

2. Install required dependencies:
```bash
pip install gradio python-dotenv langchain-community sendgrid pydantic agents
```

3. Set up environment variables in `.env` file:
```env
SENDGRID_API_KEY=your_sendgrid_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Configuration

### Email Settings
Update the email addresses in `email_agent.py`:
```python
from_email = Email('your_email@gmail.com')
to_email = To('recipient@gmail.com')
```

### Search Configuration
The system is configured to perform 3 searches per query. You can modify this in `planner_agent.py`:
```python
SEARCHES = 3  # Adjust as needed
```

## Usage

### Running the Application

1. Start the Gradio interface:
```bash
python deep_research.py
```

2. Open your browser and navigate to the provided local URL (typically `http://localhost:7860`)

3. Enter your research query in the text box

4. Click "RUN" or press Enter to start the research process

### Research Process

The system follows these steps:

1. **Query Analysis**: The planner agent analyzes your query and creates targeted search strategies
2. **Web Searching**: Multiple searches are performed concurrently using DuckDuckGo
3. **Information Synthesis**: Search results are summarized and filtered for relevance
4. **Report Generation**: A comprehensive markdown report is created with detailed analysis
5. **Email Delivery**: The report is formatted as HTML and sent via email

### Example Queries

- "Latest developments in artificial intelligence and machine learning"
- "Climate change impacts on global food security"
- "Cryptocurrency market trends and regulatory changes"
- "Remote work productivity tools and best practices"

## API Requirements

### OpenAI API
- Used for powering the AI agents
- Requires a valid OpenAI API key
- Uses GPT-4o-mini model for cost-effective operation

### SendGrid API
- Used for email delivery
- Requires SendGrid account and API key
- Supports HTML email formatting

## Output Format

### Report Structure
- **Executive Summary**: Brief overview of findings
- **Detailed Analysis**: Comprehensive examination of the topic
- **Key Findings**: Important discoveries and insights
- **Follow-up Questions**: Suggested areas for further research

### Delivery Methods
- **Web Interface**: Real-time display of the generated report
- **Email**: Formatted HTML version sent to configured email address
- **Markdown**: Raw markdown format for easy integration

## Customization

### Adding New Agents
You can extend the system by adding new specialized agents:

1. Create a new agent file following the existing pattern
2. Define the agent's instructions and tools
3. Integrate with the research manager workflow

### Modifying Search Behavior
- Adjust the number of searches in `planner_agent.py`
- Modify search summarization length in `search_agent.py`
- Change search providers by updating the search tool

### Report Customization
- Modify report structure in `writer_agent.py`
- Adjust word count requirements
- Add custom sections or analysis types

## Dependencies

- **gradio**: Web interface framework
- **python-dotenv**: Environment variable management
- **langchain-community**: Search tool integration
- **sendgrid**: Email delivery service
- **pydantic**: Data validation and serialization
- **agents**: AI agent framework (OpenAI-based)

## Error Handling

The system includes robust error handling:
- Failed searches are skipped without stopping the process
- Email delivery errors are logged but don't affect report generation
- Network issues are handled gracefully with retries

## Performance Considerations

- Searches are performed concurrently for faster execution
- Results are cached within the session
- API calls are optimized to minimize costs
- Progress tracking provides real-time feedback

## Security Notes

- Store API keys securely in environment variables
- Never commit `.env` files to version control
- Use appropriate email authentication settings
- Consider rate limiting for production deployments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
