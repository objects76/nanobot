import os

import litellm

# Langfuse configuration - MUST be set before importing litellm
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-d4ee633b-f42c-4663-b272-0d525f1a44f4"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-c2bc79a2-94f8-4fa7-b8eb-44add4a1cbd4"
os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com"
# https://us.cloud.langfuse.com/project/cmmacc8wi03o4ad062kk0bh98/traces

NANOBOT_LLMLOG = os.environ.get("NANOBOT_LLMLOG", "0") in ("yes", "true", "1")


class Langfuse:
    @staticmethod
    def setup():
        """Configure Langfuse environment variables and enable callback."""
        # Env vars are already set at module level before litellm import
        # Enable Langfuse callback if not already configured
        if not NANOBOT_LLMLOG:
            return

        if not litellm.callbacks:
            litellm.callbacks = ["langfuse"]
        elif "langfuse" not in litellm.callbacks:
            litellm.callbacks.append("langfuse")
        print(f"langfuse: nanobot | callbacks: {litellm.callbacks}")
