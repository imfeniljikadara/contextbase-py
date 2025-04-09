from contextbase.client import ContextBase

ctx = ContextBase("https://contextbase.onrender.com")

# Auth
token = ctx.login("ramulo69ramula@gmail.com", "Ramulo@69")
print("🔐 Token:", token)

# Set
ctx.set("framework", "flask")
ctx.set("language", "python")

# Get
print(ctx.get("framework"))

# List
print(ctx.list())

# Search
print(ctx.search("python"))

# Delete
print(ctx.delete("framework"))