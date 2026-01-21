# Testing checklists
In this repo there is an issue template for regression testing. These issue
templates are used in the [Archivematica Issues
repository](https://github.com/archivematica/Issues) when we do regression
testing for a release.

The issue template is generated from the **regression-testing-checklist.csv**
file in this repository.

## Generate the template with Python

Run the provided script from the repository root:

```bash
python3 generate_issue_template.py
```

The script only depends on the Python standard library. It reads
`regression-testing-checklist.csv` and overwrites
`.github/ISSUE_TEMPLATE/issue_template.md` with the rendered template using the
same formatting as the OpenRefine workflow. Use the `--csv` or `--output`
arguments if you need to point to different files.

## Legacy OpenRefine workflow

If you prefer to regenerate the file manually, follow the previous process:

1. Load the CSV into OpenRefine
2. Apply changes/cleanup as needed
   * Remove unneeded columns
   * Facet Functional Area by text, then select each choice to isolate rows,
   then blank down so that only the top row has the Functional Area name (this
   makes it easier to delete duplicate headings later)
3. Export the data by going to Export > Templating
4. Paste data from [this
   gist](https://gist.github.com/sallain/5a7c54d256ab17eb04a202332594798e)
   into the template and export (leave Row separator and Suffix fields blank)
5. Tidy up markdown file
   * Remove duplicate headings by finding `## null` and replacing with nothing

In the [Archivematica Issues repository](https://github.com/archivematica/Issues),
replace the testing-checklist issue template with your new markdown file.
