# Testing checklists
In this repo there is an issue template for regression testing. By creating an
issue using this template, testers have a checklist of specific tests to run.
Issues should be created per environment.

The issue template is generated from the **regression-testing-checklist.csv**
file in this repository. To create a new issue template:

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
