# ContextBase Python SDK

A Python SDK for interacting with the ContextBase MCP API, simple key-value memory storage service with authentication and search capabilities.

## Installation

```bash
pip install contextbase-py
```

## Usage

### Initialization

```python
from contextbase import Context

ctx = Context(base_url='https://contextbase.onrender.com')
```

### Authentication

```python
signup_token = ctx.signup('user@example.com', 'password')

login_token = ctx.login('user@example.com', 'password')

ctx.set_token('your-auth-token')
```

### Memory Operations

```python
ctx.set('myKey', 'myValue')

ctx.set('temporaryKey', 'temporaryValue', 3600)  # 1 hour TTL
ctx.set('temporaryKey', 'temporaryValue')  # Without TTL

memory = ctx.get('myKey')

all_memories = ctx.list()

search_results = ctx.search('queryString')

ctx.delete('myKey')
```

## API Reference

### Constructor

```python
Context(
    base_url: str,
    token: str = None  # Optional initially, required for memory operations
)
```

### Methods

| Method | Parameters | Return Type | Description |
|--------|------------|-------------|-------------|
| `set_token` | `token: str` | `None` | Sets the authentication token |
| `signup` | `email: str, password: str` | `str` | Creates a new user account and returns a token |
| `login` | `email: str, password: str` | `str` | Authenticates user and returns a token |
| `set` | `key: str, value: str, ttl: int = None` | `dict` | Stores a memory with optional TTL (in seconds) |
| `get` | `key: str` | `dict` | Retrieves a memory by key |
| `list` | None | `list` | Lists all memories |
| `search` | `query: str` | `list` | Searches memories by query string |
| `delete` | `key: str` | `dict` | Deletes a memory by key |


## License

MIT
