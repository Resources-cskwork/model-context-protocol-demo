# Model Context Protocol Demo

This is a demo project showcasing the Model Context Protocol (MCP) with a SQLite database integration.

## Prerequisites

- macOS or Windows
- The latest version of Claude Desktop installed
- uv 0.4.18 or higher (uv --version to check)
- Git (git --version to check)
- SQLite (sqlite3 --version to check)

### Installing prerequisites (Windows)

```bash
# Using winget
winget install --id=astral-sh.uv -e
winget install git.git sqlite.sqlite

# Or download directly:
# uv: https://docs.astral.sh/uv/
# Git: https://git-scm.com
# SQLite: https://www.sqlite.org/download.html
```

### Installing prerequisites (macOS)

```bash
# Using Homebrew
brew install uv git sqlite3
```

## Setup

1. Install prerequisites:
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

2. Create the SQLite database:
   ```bash
   python create_db.py
   ```

3. Configure Claude Desktop:
   - Open `%APPDATA%\Claude\claude_desktop_config.json`
   - Add the following configuration:

   db
   ```json
   {
     "mcpServers": {
       "sqlite": {
         "command": "uvx",
         "args": [
           "mcp-server-sqlite",
           "--db-path",
           "FULL_PATH_TO_YOUR_test.db"
         ]
       }
     }
   }
   ```
   Replace `FULL_PATH_TO_YOUR_test.db` with the actual path to your test.db file.

   desktop 
  ```json 
    {
    "mcpServers": {
      "filesystem": {
        "command": "C:\\Program Files\\nodejs\\node.exe",
        "args": ["D:\\Projects\\model-context-protocol-demo\\node_modules\\@modelcontextprotocol\\server-filesystem\\dist\\index.js", 
          "C:/test/"],
        "env": {
          "NODE_ENV": "production"
        }
      }
    }
  }
    ```



4. Restart Claude Desktop

## Testing

1. Open Claude Desktop
2. Click the 🔌 icon next to the chat box
3. Expand "Installed MCP Servers" to verify the SQLite server is listed
4. Try asking Claude: "Can you connect to my SQLite database and tell me what products are available, and their prices?"

## Database Schema

The database contains a `products` table with the following structure:
- id: INTEGER PRIMARY KEY
- name: TEXT
- price: REAL

Sample data includes various tech products with their prices.
