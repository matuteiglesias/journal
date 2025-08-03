---
title: "Configured Jupyter and Linux Environment Paths"
tags: ['Jupyter', 'Linux', 'Environment Setup', 'Vs Code', 'Notebook Conversion']
created: 2023-01-12
publish: true
---

## 📅 2023-01-12 — Session: Configured Jupyter and Linux Environment Paths

**🕒 13:00–13:35**  
**🏷️ Labels**: Jupyter, Linux, Environment Setup, Vs Code, Notebook Conversion  
**📂 Project**: Dev  
**⭐ Priority**: MEDIUM  


### Session Goal:
The session aimed to configure environment paths in Linux and manage [[Jupyter]] Notebook cell execution and conversion settings.

### Key Activities:
1. **Adding Directory to PATH in Linux:**
   - Instructions were provided for adding the directory `/home/matias/.local/bin` to the PATH environment variable for both bash and zsh shells.
   - Steps included applying changes and alternatives for temporary addition.

2. **Adding Interactive-Only Tags in [[Jupyter]] Notebooks:**
   - Steps were outlined to add 'interactive-only' tags to cells in [[Jupyter]] notebooks using Visual Studio Code.
   - Instructions were given for exporting the notebook to a script while excluding tagged cells.

3. **Preventing Code Execution in [[Jupyter]] Notebooks:**
   - Discussed methods to include code in exported [[Python]] scripts from [[Jupyter]] notebooks without executing it when running all cells.
   - Techniques included using the `#%%` cell magic command and wrapping code in functions.

4. **Resolving Unrecognized Flag Error in [[Jupyter]]:**
   - Addressed the error `Unrecognized flag: '--tag'` in the `jupyter nbconvert` command.
   - Solutions included upgrading [[Jupyter]] or using the `jupyter_execute_notebook` package.

5. **Using TagRemovePreprocessor in [[Jupyter]] Notebook:**
   - Explained the use of the `--TagRemovePreprocessor.remove_cell_tags` flag to exclude cells with specific tags during script conversion.
   - Provided command examples and noted version availability.

### Achievements:
- Successfully configured environment paths and managed cell execution settings in [[Jupyter]] Notebooks.
- Resolved conversion errors and improved script export processes.

### Pending Tasks:
- Verify the effectiveness of the changes in a live environment and document any further adjustments needed.
