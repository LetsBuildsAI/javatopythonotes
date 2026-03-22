# Java → Python notes

Small Python package layout for learning. **Java analogies:**

| Java | Python (this repo) |
|------|---------------------|
| `pom.xml` / `build.gradle` | `pyproject.toml` |
| `src/main/java/com/example/` | `src/javatopythonotes/` |
| `src/test/java/` | `tests/` |
| `public static void main` | `python -m javatopythonotes` or a `main()` in a script |

## Setup

```bash
cd javatopythonotes
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"
```

Activate the venv in every new terminal before running the commands below.

## Tests

From the `javatopythonotes` directory (with venv active and package installed):

```bash
pytest
```

Useful variants:

```bash
pytest -q
pytest tests/test_helloworld.py
pytest tests/test_jsonplaceholder.py
pytest tests/test_control_flow_examples.py
pytest tests/test_data_structures_examples.py
pytest tests/test_functions_advanced_examples.py
pytest tests/test_classes_examples.py
pytest tests/test_exceptions_examples.py
pytest tests/test_imports_examples.py
pytest tests/test_file_io_examples.py
pytest tests/test_generators_examples.py
pytest tests/test_context_manager_examples.py
pytest tests/test_javatopythonotes.py
```

If you have **not** run `pip install -e .`, set `PYTHONPATH=src` (same as in `pyproject.toml` for pytest):

```bash
PYTHONPATH=src pytest
```

## Run example modules

Each line runs that package’s `__main__.py`. Omit `PYTHONPATH=src` after `pip install -e .`.

### Root package

```bash
python -m javatopythonotes
```

### Basics

```bash
python -m javatopythonotes.helloworld
python -m javatopythonotes.jsonplaceholder
```

`jsonplaceholder` calls the public internet; skip it if you are offline.

### Control flow

```bash
python -m javatopythonotes.if_examples
python -m javatopythonotes.for_examples
python -m javatopythonotes.while_examples
python -m javatopythonotes.switch_examples
```

### Data, functions, classes, errors, imports, IO, generators, context managers

```bash
python -m javatopythonotes.data_structures_examples
python -m javatopythonotes.functions_advanced_examples
python -m javatopythonotes.classes_examples
python -m javatopythonotes.exceptions_examples
python -m javatopythonotes.imports_examples
python -m javatopythonotes.file_io_examples
python -m javatopythonotes.generators_examples
python -m javatopythonotes.context_manager_examples
```

### Run every module in one go (copy-paste)

```bash
python -m javatopythonotes
python -m javatopythonotes.helloworld
python -m javatopythonotes.jsonplaceholder
python -m javatopythonotes.if_examples
python -m javatopythonotes.for_examples
python -m javatopythonotes.while_examples
python -m javatopythonotes.switch_examples
python -m javatopythonotes.data_structures_examples
python -m javatopythonotes.functions_advanced_examples
python -m javatopythonotes.classes_examples
python -m javatopythonotes.exceptions_examples
python -m javatopythonotes.imports_examples
python -m javatopythonotes.file_io_examples
python -m javatopythonotes.generators_examples
python -m javatopythonotes.context_manager_examples
```

Without editable install, prefix commands with `PYTHONPATH=src`, for example:

```bash
PYTHONPATH=src python -m javatopythonotes.helloworld
```
