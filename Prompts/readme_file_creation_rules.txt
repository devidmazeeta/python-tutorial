# README.md File Creation Rules for python-tutorial

## 1. Read the Repository Structure First
- Start by scanning the repository:
  link: https://github.com/devidmazeeta/python-tutorial
- Identify:
  - All folders, subfolders, and files (.py)
  - Hierarchy: 01_Introduction_to_Python, 02_Basic_Python_Syntax, 03_Data_Structures, etc.
- Detect program files to auto-populate Learning Order of Programs.

## 2. File Naming and Location
- Create README.md for each section.
- Place at the root of that section’s folder, e.g., ./03_Data_Structures/README.md.

## 3. Standard Sections in Each README
- Title: "# Chapter X: <Section Title>"
- Introduction: Short overview of content and purpose.
- Learning Objectives: Bullet list of outcomes.
- Learning Order of Programs:
    - List discovered program files with relative links:
      1. ../03_Data_Structures/numeric.py
      2. ../03_Data_Structures/boolean.py
      3. ../03_Data_Structures/sequencetype.py
      4. ../03_Data_Structures/dictionary.py
      5. ../03_Data_Structures/setdatatype.py
- Concept Overview (optional):
    - Add diagrams or images with relative paths.
- Detailed Notes:
    - Use headings and code examples.
- Exercises:
    - Provide practice tasks.
- Next Steps:
    - Link to the next chapter, e.g., ../04_Control_Flow/README.md.

## 4. Linking and Paths
- Always use relative paths: ../
- Include folder and file name.
- Keep images in the same folder or subfolder and link relatively.

## 5. Code and Formatting
- Use fenced code blocks for Python examples.
- Follow PEP 8 style.
- Inline code for keywords and commands.

## 6. Consistency and Readability
- Maintain consistent style, tone, and formatting.
- Use clear Markdown features: headings, lists, bold/italic.

## 7. Automation (Recommended Best Practice)
- Automate README generation:
    - Read repo structure from https://github.com/devidmazeeta/python-tutorial
    - Detect .py files in each folder.
    - Populate README sections using a standard template.
