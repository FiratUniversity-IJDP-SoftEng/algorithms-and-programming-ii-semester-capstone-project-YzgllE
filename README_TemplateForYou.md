# Rabin-Karp Visualizer - Interactive Visualization

## Project Overview

This project is an interactive web application that implements and visualizes the **Rabin-Karp string searching algorithm**, developed as part of the Algorithms and Programming II course at Fırat University, Software Engineering Department.

## Algorithm Description

### Problem Definition

The Rabin-Karp algorithm solves the **exact string matching** problem. Given a text `T` of length `n` and a pattern `P` of length `m`, the algorithm searches for all occurrences of `P` in `T`.

### Mathematical Background

- The algorithm uses a **rolling hash** function to efficiently compare substring hashes.
- A polynomial hash function is used:\
  \(h(s) = (s[0] \cdot d^{m-1} + s[1] \cdot d^{m-2} + ... + s[m-1]) \mod q\) where:
  - `d` is the number of characters in the input alphabet (e.g., 256 for ASCII)
  - `q` is a large prime number to reduce hash collisions

### Algorithm Steps

1. Compute the hash value of the pattern `P`.
2. Compute the hash value of the first substring of `T` with length `m`.
3. Compare the hash values:
   - If equal, compare the strings character by character.
   - If unequal, skip.
4. Slide the window over text using the rolling hash formula:
   - Subtract the leading digit
   - Multiply remaining hash by `d`
   - Add new trailing character
5. Repeat steps 3-4 until the end of the text.

### Pseudocode

```python
function RabinKarp(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q
    p = 0  # pattern hash
    t = 0  # text hash

    # Initial hash
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                print("Pattern occurs at index", s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
```

## Complexity Analysis

### Time Complexity

- **Best Case:** O(n + m) - No hash collisions
- **Average Case:** O(n + m) - Few hash collisions
- **Worst Case:** O(nm) - All hash values match but actual strings differ

### Space Complexity

- O(1) additional space (excluding input and output)

## Features

- Visualizes the rolling hash computation step-by-step
- Highlights matching substrings
- Interactive pattern input
- Fast pattern lookup in long text inputs

## Screenshots

![Main Interface](<screenshoots/Screenshot 2025-06-22 182152.png>)

![Algorithm in Action](<screenshoots/Screenshot 2025-06-22 182212.png>)

![Algorithm in Action](<screenshoots/Screenshot 2025-06-22 182222.png>)

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rabin-karp-visualizer.git
   cd rabin-karp-visualizer
   ```

2. Create a virtual environment:

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Enter the text string in the input area.
2. Enter the pattern string to search.
3. Press "Run Rabin-Karp" to start visualization.
4. Step through the matching process interactively.

### Example Inputs

- **Example 1:**

  - Text: `GEEKS FOR GEEKS`
  - Pattern: `GEEK`
  - Output: Pattern found at index 0 and 10

- **Example 2:**

  - Text: `ABABDABACDABABCABAB`
  - Pattern: `ABABCABAB`
  - Output: Pattern found at index 10

- **Example 3:**

  - Text: `THE QUICK BROWN FOX`
  - Pattern: `FOX`
  - Output: Pattern found at index 16

## Implementation Details

### Key Components

- `algorithm.py`: Contains the core Rabin-Karp algorithm
- `app.py`: Streamlit UI logic
- `utils.py`: Utility functions for hash and rolling logic
- `visualizer.py`: Functions for visual step-by-step output

### Code Highlights

```python
def rabin_karp(text, pattern, d=256, q=101):
    """
    Searches for occurrences of `pattern` in `text` using Rabin-Karp
    """
    m, n = len(pattern), len(text)
    h = pow(d, m-1) % q
    p = t = 0
    result = []

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t and text[s:s+m] == pattern:
            result.append(s)
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return result
```

## Testing

This project includes a test suite to verify correctness:

```bash
python -m unittest test_algorithm.py
```

### Test Cases

- Pattern exists once at beginning
- Pattern exists multiple times
- Pattern not found
- Pattern equals text

## Live Demo

A live demo of this application is available at: [https://algorithms-and-programming-ii-semester-capstone-project-yzglle.streamlit.app]

## Limitations and Future Improvements

### Current Limitations

- Performance may degrade on extremely large inputs
- Limited support for unicode text
- Only exact match (no fuzzy matching)

### Planned Improvements

- Add fuzzy matching capability
- Enhance visual feedback with animations
- Export results as JSON/CSV

## References and Resources

### Academic References

1. Cormen, Leiserson, Rivest, and Stein. *Introduction to Algorithms*.
2. Gusfield, D. *Algorithms on Strings, Trees and Sequences*.
3. Rabin, M. O., and Karp, R. M. (1987). *Efficient randomized pattern-matching algorithms.*

### Online Resources

- [https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp\_algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
- [https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/](https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/)
- [https://visualgo.net/en/string](https://visualgo.net/en/string)

## Author

- **Name:** Yusuf Emre Yüzügüllü
- **Student ID:** [230543020]
- **GitHub:** (https://github.com/YzgllE)

## Acknowledgements

I would like to thank Assoc. Prof. Ferhat UÇAR for guidance throughout this project.

---

*This project was developed as part of the Algorithms and Programming II course at Fırat University, Technology Faculty, Software Engineering Department.*

