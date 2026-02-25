# import and run pipeline
# exit with appropriate status code
from src.config import Config
from src.pipeline import run_pipeline

if __name__ == "__main__":
    Config.validate()
    try:
        run_pipeline()
        exit(0)
    except Exception as e:
        print(f"Error running pipeline: {e}")
        exit(1)