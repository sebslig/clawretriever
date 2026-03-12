import os
from clawretriever.engine import RagPipeline

def main():
    # Setup dummy data for demonstration
    os.makedirs("demo_docs", exist_ok=True)
    with open("demo_docs/guide.txt", "w") as f:
        f.write("ClawRetriever is an AI tool for building RAG applications using OpenClaw agents.")
    
    # Run pipeline
    pipeline = RagPipeline(data_dir="demo_docs")
    response = pipeline.ask("What is ClawRetriever?")
    
    print("-" * 30)
    print(f"QUERY: What is ClawRetriever?")
    print(f"ANSWER: {response}")
    print("-" * 30)

if __name__ == "__main__":
    main()
