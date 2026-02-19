"""Allows running the package directly: python -m mcp_sharepoint"""
import asyncio

from .server import main

asyncio.run(main())
