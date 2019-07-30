# Testing checklists
In this repo there is an issue template for regression testing. By creating an issue using this template, testers have a checklist of specific tests to run. Issues should be created per environment.

The issue template is generated from the **AMAUAT Gap Analysis - Regression Testing Checklist** (stored in Artefactual Google Drive). To create a new issue template:

1. Export the checklist from Google Drive as a CSV
2. Load the CSV into OpenRefine
3. Apply changes/cleanup as needed
   * Remove unneeded columns
   * Facet Functional Area by text, then select each choice to isolate rows, then blank down so that only the top row has the Functional Area name (this makes it easier to delete dupe headings later)
   * Add - [ ] to beginning of feature cells
4. Export the data by going to Export > Templating
5. Paste data from [this gist](https://gist.github.com/sallain/5a7c54d256ab17eb04a202332594798e) into the template and export (leave Row separator and Suffix fields blank)
6. Tidy up markdown file
   * Remove duplicate headings by finding `## null` and replacing with nothing
