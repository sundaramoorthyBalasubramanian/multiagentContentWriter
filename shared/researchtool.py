import json
from langchain_core.tools import tool


@tool
def research_tool(topic: str):
    """
    Mock research tool.

    Returns research articles, statistics, expert opinions,
    references, FAQs, and case studies related to the topic.
    """

    research_results = {
        "topic": topic,
        "articles": [
            {
                "title": f"Complete Guide to {topic}",
                "author": "John Smith",
                "source": "Tech Insights",
                "year": 2025,
                "summary": f"A comprehensive introduction covering the fundamentals of {topic}.",
                "url": "https://example.com/article1"
            },
            {
                "title": f"Latest Trends in {topic}",
                "author": "Emily Johnson",
                "source": "AI Today",
                "year": 2026,
                "summary": f"Discusses the latest developments and industry trends in {topic}.",
                "url": "https://example.com/article2"
            },
            {
                "title": f"Best Practices for {topic}",
                "author": "David Brown",
                "source": "Developer Weekly",
                "year": 2025,
                "summary": f"Recommended implementation strategies and common pitfalls.",
                "url": "https://example.com/article3"
            }
        ],
        "statistics": [
            "82% of organizations plan to increase investment in AI over the next two years.",
            "Companies adopting AI-powered automation report productivity improvements of up to 35%.",
            "Demand for AI-related skills has increased significantly in recent years."
        ],
        "expert_opinions": [
            "AI agents are evolving from assistants to autonomous collaborators.",
            "Retrieval-Augmented Generation improves factual accuracy for enterprise AI systems.",
            "Human oversight remains essential for critical AI decision making."
        ],
        "case_studies": [
            {
                "company": "ABC Retail",
                "result": "Reduced customer support response time by 60% using AI agents."
            },
            {
                "company": "XYZ Finance",
                "result": "Automated document processing with 92% accuracy."
            }
        ],
        "faqs": [
            f"What is {topic}?",
            f"How does {topic} work?",
            f"What are the benefits of {topic}?",
            f"What are the challenges of {topic}?",
            f"What are the future trends in {topic}?"
        ],
        "references": [
            "https://example.com/reference1",
            "https://example.com/reference2",
            "https://example.com/reference3"
        ]
    }

    return json.dumps(research_results, indent=2)