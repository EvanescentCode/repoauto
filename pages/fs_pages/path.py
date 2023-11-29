from pathlib import Path


class Paths:
    BASIC_ROOT = Path(__file__).parent.parent.parent
    TEST_FOLDER = BASIC_ROOT / "testcases"
    DATA_FOLDER = TEST_FOLDER / "data"

    @classmethod
    def test_data(cls, test_data: str) -> Path:
        return cls.DATA_FOLDER / f"{test_data}.json"