from shared.researchtool import research_tool
from shared.internetsearchtool import internet_search_tool
from shared.routerllm import router_llm

seo_tools = [research_tool, internet_search_tool]
# Bind tools to the LLM
seo_blog_llm = router_llm.bind_tools(
    [
        research_tool,
        internet_search_tool,
    ]
)

x_tools = [ internet_search_tool]
# Bind only the internet search tool
x_writer_llm = router_llm.bind_tools(
    [
        internet_search_tool,
    ]
)