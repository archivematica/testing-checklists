---
name: Testing checklist template
about: Use this template to create an issue for regression testing
---

### 1. Transfer Types

1.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Process a Standard transfer using SampleTransfers/Images. Validate the METS.
  - [ ] All standard AIP structure and METS structure criteria apply (see Create AIP)

1.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] process an Unzipped Bag transfer using SampleTransfers/BagTransfer. The bag should verify during “Job: Verify bag, and restructure for compliance”. Validate the METS.
  - [ ] All standard AIP structure and METS structure criteria apply. AND
  - [ ] The Bag Verification microservice executes successfully AND
  - [ ] (Optionally) The contents of bag-info.txt are translated to METS

#### 1.3

**Severity**: High

**Current test coverage**: none

**External tools**: 7zip

- [ ] process a Zipped Bag transfer using SampleTransfer/BagTransfer.zip. The bag should verify during “Job: Verify bag, and restructure for compliance”. Validate the METS.
  - [ ] All standard AIP structure and METS structure criteria apply. AND
  - [ ] The Bag Verification microservice executes successfully AND
  - [ ] (Optionally) The contents of bag-info.txt are translated to METS

#### 1.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] process a DSpace transfer using SampleTransfer/DSpaceExport (or one of the zips contained inside). All DSpace-specific microservices should succeed. Validate the METS.
  - [ ] As above; all standard criteria + list out Dspace microservices

#### 1.5

**Severity**: Medium

**Current test coverage**: none

**External tools**: tsk_recover (Sleuthkit); unrar-free

- [ ] process a Disk Image transfer using SampleTransfer/ISODiskImage. Before starting the transfer, add disk image metadata. Validate the METS.
  - [ ] Disk image metadata ends up in the AIP METS.

#### 1.6

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] process the three Dataverse transfers separately (SampleTransfers/Dataverse/AStudyOfMyAfternoonDrinks, SampleTransfers/Dataverse/NDSAStaffingReport, SampleTransfers/Dataverse/XRayScansOfPolyodonSpathula). Make sure that Archivematica is NOT set to delete packages after extraction. “Job: parse external files” should succeed. Validate the METS.
  - [ ] Dataverse metadata is translated to METS, e.g. DDI information for author and institution.

### 2. Transfer Variants

#### 2.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Process a transfer using SampleTransfer/DemoTransfer. The AIP METS should contain metadata from the description and rights CSVs.
  - [ ] Submission documentation should be preserved and listed in the AIP METS with the correct file group use (it should be fileGrp USE="submissionDocumentation")

#### 2.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a Transfer includes Submission Documentation using a submissionDocumentation directory
  - [ ] Submission documentation should be preserved and listed in the AIP METS with the correct file group use (it should be fileGrp USE="submissionDocumentation")

#### 2.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer contains descriptive metadata for directories (multi-level) using a metadata.csv (use SampleTransfer/CSVmultiLevel).  
  - [ ] The AIP METS will contain descriptive metadata against for each of the directories described in the metadata.csv

#### 2.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer contains descriptive metadata for individual files using a metadata.csv
  - [ ] The AIP METS will contain descriptive metadata against for each of the files described in the metadata.csv

#### 2.5

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Change your processing config: set “Normalization” to None and “Approve normalization” to None. Process a transfer using TestTransfers/ManualNormalization. At Normalization, choose “Normalize for preservation and access”.
  - [ ] Originals (denoted in the METS fileSec) should be .dat, .TGA, and .GIF; preservation copies should be .prk, .tif, and .tif; AND
  - [ ] Access copies (denoted in the METS fileSec) should be .bmp, .jpg, and .jpg.

#### 2.6

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Change your processing config: set “Normalization” to None and “Approve normalization” to None. Process a transfer using SampleTransfers/transfer-with-access-copies. “Job: Normalize” should only give three options - choose “Normalize for preservation”.
  - [ ] Originals should be .png, preservation copies should be as per rule, AND
  - [ ] access copies should be .bmps

#### 2.7

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Change your processing config: set “Normalization” to None and “Approve normalization” to None. Run service-files transfer and choose “Normalize service files for access”.
  - [ ] "Job Normalize service files for access" should run AND
  - [ ] the task output should show that the service files were used to create access copies.

#### 2.8

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When a Processing Configuration xml file is included in a Transfer
  - [ ] then the Transfer and Ingest processing will follow the decisions set out in the processing configuration xml file

#### 2.9

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] When structural metadata is included in a Transfer using a mets_structmap.xml file
  - [ ] Then the provided structural map will be included in the AIP METs file.

### 3. Checksums & Integrity Checking

#### 3.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer includes invalid external checksums
(Test using TestTrasnfers/fixityCheckShouldFail)
  - [ ] Then the job "metadata directory checksums" has a FAILED status
  - [ ] Stdout/Stderr describe which checksums failed
  - [ ] The Failed Transfer microservice is triggerd

#### 3.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer includes valid external checksums
(Test using DemoTransfer)
  - [ ] Then the job "metadata directory checksums" has a COMPLETED status
  - [ ] Stdout/Stderr describe the validation check

#### 3.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a SIP includes valid checksums (i.e. created by Archivematica during Transfer processing)
  - [ ] then the microservice "Verify Checksums" has completed sucessfully

#### 3.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a SIP has been corrupted
(test by replacing a file in the SIP after Transfer but before Ingest processing)
  - [ ] The Ingest Microservice "Verify checksums" has a FAILED status
  - [ ] The "Failed SIP" microservice is triggered

### 4. Virus scanning & quarantine

#### 4.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Given a transfer that contains a virus
When the Virus checkingmicroservice is executed
(testing using TestTransfers/virusTests)
  - [ ] The task Scan for Viruses will fail AND
  - [ ] The microservice will record a failure, because of a virus for each, i.e. it shouldn't report other errors such as MAXSTREAMLENGTH

#### 4.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Given a transfer that does NOT contain a virus
When the Virus checkingmicroservice is executed
(testing using TestTransfers/virusTests)
  - [ ] The task Scan for Viruses will pass AND

#### 4.3

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Quarantine and unquarantine a “good” transfer manually
  - [ ] The transfer should continue AND
  - [ ] A quarantine PREMIS event should be created with today's date should be created

#### 4.4

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Quarantine and unquarantine a “bad” transfer manually

#### 4.5

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Set a # of days for quarantine in processing config and check back once time has elapsed
  - [ ] The transfer registers as in quarantine AND
  - [ ] After <elapsed_time> the transfer continues and an AIP is created AND
  - [ ] The AIP will contain a quarantine event

#### 4.6

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Reject quarantined transfer
  - [ ] The transfer status is REJECTED AND
  - [ ] The transfer is available in the rejected directory

### 5. Package Extraction

#### 5.1

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer includes a package object (e.g. .zip) and the processing configuration is set to Extract Packages....
(Test with SampleTransfers/OfficeDocs.)
  - [ ] ZIPs should unpack properly AND
  - [ ] An unpacking event is registered in PREMIS AND
  - [ ] Characterisation and validation events exist for the extracted contents AND
  - [ ] And a directory (nested directories) are created reflecting the structure of the zip AND
  - [ ] That directory has a timestamp suffix

#### 5.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Fail some transfers using TestTransfers/broken_package_format_types.
  - [ ] Transfer status will be marked as FAILED
  - [ ] And the job that it FAILED on matches our expectations AND
  - [ ] The transfer should be in the failed directory

#### 5.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer includes a package object (e.g. .zip) and the processing configuration is set to Extract Packages ANd the processing configuration is set to delete packages after extraction....
(Test with SampleTransfers/OfficeDocs.)
  - [ ] As above, AND
  - [ ] the original package file no longer exists in the downloaded AIP

#### 5.4

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When a transfer includes a package object (e.g. .zip) AND the processing configuration is set to Extract Packages AND the processing configuration is set to retain packages after extraction....
(Test with SampleTransfers/OfficeDocs.)
  - [ ] As above, AND
  - [ ] the original package file is present in the downloaded AIP

### 6. File Identification

#### 6.1

**Severity**: High

**Current test coverage**: none

**External tools**: Siegfried

- [ ] Process a transfer using Siegfried and check file ID results.
  - [ ] Siegfried shows in the PREMIS event detail and the version information is accurate

#### 6.2

**Severity**: High

**Current test coverage**: none

**External tools**: Siegfried

- [ ] Given a transfer includes the known format xxyy
When Siegfried is used for file identification
  - [ ] There is a File Identification PREMIS event
  - [ ] The "Siegried" tool and version number is described in the PREMIS event detail
  - [ ] The file is described as being of format xxyy

#### 6.3

**Severity**: High

**Current test coverage**: none

**External tools**: Siegfried

- [ ] Given a transfer includes the unknown format xxyy
When Siegfried is used for file identification
  - [ ] As above, and:
  - [ ] The file is described as being of unknown format

#### 6.4

**Severity**: High

**Current test coverage**: none

**External tools**: Fido

- [ ] Process a transfer using FIDO and check file ID results.
  - [ ] Fido shows in the PREMIS event detail and the version information is accurate

#### 6.5

**Severity**: High

**Current test coverage**: none

**External tools**: Fido

- [ ] Given a transfer includes the known format xxyy When FIDO is used for file identification
  - [ ] There is a File Identification PREMIS event
  - [ ] The "FIDO" tool and version number is described in the PREMIS event detail
  - [ ] The file is described as being of format xxyy

#### 6.6

**Severity**: High

**Current test coverage**: none

**External tools**: Fido

- [ ] Given a transfer includes the unknown format xxyy
When FIDO is used for file identification
  - [ ] There is a File Identification PREMIS event
  - [ ] The "FIDO" tool and version number is described in the PREMIS event detail
  - [ ] The file is described as being of format xxyy

#### 6.7

**Severity**: High

**Current test coverage**: none

**External tools**: File extension script

- [ ] Process a transfer using file extension and check file ID results.
  - [ ] <premis:eventType>format identification</premis:eventType> is:
~~~~
<premis:eventDetailInformation> is "program="File Extension"; version="0.1" and
~~~~
  - [ ] <premis:eventOutcome> is "positive"

#### 6.8

**Severity**: Medium

**Current test coverage**: none

**External tools**: File extension script

- [ ] Process a transfer and skip file ID and check file ID results.
  - [ ] Job: Identify File Format has stdout = "Skipping file format identification"
  - [ ] there is no <premis:eventType>format identification</premis:eventType> in the METS

### 7. Validation

#### 7.1

**Severity**: High

**Current test coverage**: none

**External tools**: JHOVE

- [ ] Validation: While processing above transfers, check the validation output for a variety of formats to ensure that it’s reporting accurate information.
  - [ ] Job: Validate formats has exit code = "0"
  - [ ] <premis:eventType>validation</premis:eventType> is present in the METS
  - [ ] eventOutcomeDetailNote contains the value "Well-Formed and valid, e.g.
~~~~
<premis:eventOutcomeDetailNote>format="TIFF"; version="4.0"; result="Well-Formed and valid"</premis:eventOutcomeDetailNote>
~~~~

#### 7.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: MediaConch

- [ ] Check MediaConch by processing SampleTransfers/Matroska and checking the validation output.
  - [ ] Job: Validate formats has stdout = "Running Validate using MediaConch Command "Validate using MediaConch" was successful"
  - [ ] <premis:eventType>validation</premis:eventType> is present in the METS
  - [ ] premis:eventDetail indicates that MediaConch was used, eg.
~~~~
<premis:eventDetailInformation><premis:eventDetail>program="MediaConch"; version="18.03"</premis:eventDetail>
~~~~

#### 7.3

**Severity**: Low

**Current test coverage**: none

**External tools**: MediaConch

- [ ] Policy check on originals: create a MediaConch policy by following the instructions in the docs
  - [ ] make sure that validation event is added to the METS that contains policy check information.

### 8. Characterization

#### 8.1

**Severity**: High

**Current test coverage**: none

**External tools**: FFprobe, ExifTool, MediaInfo, FITS, fiwalk (Sleuthkit)

- [ ] Characterization: While processing above transfers, check the validation output for a variety of formats to ensure that it’s reporting accurate information.
  - [ ] Job: Characterize and extract metadata has stdout that contains:
  - [ ] "Saved XML output for command "FFprobe""
  - [ ] "Saved XML output for command "ExifTool"
  - [ ] "Saved XML output for command "MediaInfo"
  - [ ] "Saved XML output for command "FITS"
- [ ] extracted XML metadata is present in the <premis:objectCharacteristicsExtension> element in the METS file.

### 9. Normalization

#### 9.1

**Severity**: High

**Current test coverage**: none

**External tools**: ffmpeg, convert (ImageMagick), ps2pdf, inkscape, Ghostcsript

- [ ] Make sure that all normalization types work
  - [ ] normalize for preservation and access
  - [ ] normalize for preservation
  - [ ] reject SIP
  - [ ] normalize service files for access
  - [ ] do not normalize
  - [ ] normalize manually
  - [ ] normalize for access
- [ ] normalization report output = Preservation normalization attempted "yes" ; Preservation normalization failed "no" ; Preservation conformance check "passed" ; Access normalization attempted "yes" ; Access normalization failed "no" ; Access conformance check "passed"
- [ ] <premis:eventType>normalization</premis:eventType> is present in the METS for the affected files.

#### 9.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: convert (ImageMagick)

- [ ] Make sure that all thumbnail options work
  - [ ] Yes
  - [ ] Yes, without default
  - [ ] No
  - [ ] Job: Normalize for thumbnails is "successful", eg. "Successfully normalized  Club-Report.doc for thumbnail"

#### 9.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: Tesseract

- [ ] Run SampleTransfers/OCRImage and select Yes for Transcribe files (OCR)
  - [ ] The AIP contains the file "/metadata/OCRfiles/abroadcrane.... "

### 10. Sanitize Names & Special Characters

#### 10.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Sanitize names: Transfer a name sanitize sample set
  - [ ] Job: Sanitize object's file and directory names contains stdout with "Sanitized name:" outputs, e.g.
~~~~
Sanitized name: %transferDirectory%objects/pound#pound.txt  ->  %transferDirectory%objects/pound_pound.txt
Sanitized name: %transferDirectory%objects/$/control.txt  ->  %transferDirectory%objects/__9/control.txt
Sanitized name: %transferDirectory%objects/ends with a space /control.txt  ->  %transferDirectory%objects/ends_with_a_space_/control.txt
Sanitized name: %transferDirectory%objects/lessthan<.txt  ->  %transferDirectory%objects/lessthan_.txt
~~~~
  - [ ] premis:eventType "name cleanup" is present in the METS file where <premis:eventDetail> contains value "prohibited characters removed:program="sanitize_names""

#### 10.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Create a transfer with diacritics in the transfer name
  - [ ] Job: Sanitize object's file and directory names contains stdout with "Sanitized name:" outputs, e.g.
~~~~
Sanitized name: %transferDirectory%objects/ぽっぷるメイル/shift-jis_encoded_dirs.txt  ->  %transferDirectory%objects/potsupurumeiru/shift-jis_encoded_dirs.txt
~~~~
  - [ ] premis:eventType "name cleanup" is present in the METS file where <premis:eventDetail> contains value "prohibited characters removed:program="sanitize_names""

#### 10.3

**Severity**: Low

**Current test coverage**: none

**External tools**: Bulk Extractor

- [ ] Select Yes at Examine contents for SampleTransfers/DemoTransfer and then send the transfer to backlog.
  - [ ] In the Appraisal tab, check the Analysis pane for Examine contents data.

### 11. Performance & Resilience

#### 11.1

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Process multiple transfers at once.

#### 11.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Process a transfer with a large number of files (10,000 ? )

#### 11.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Process a transfer that takes up a large amount of disk space (20Gb?)

#### 11.4

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] We could add a variety of failure scenarios here -- e.g. if SS is down? or elasticSearch etc?

#### 11.5

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Failure scenario for Disk Full? perhaps just need a placeholder for this, until Disk Full changes are introduced?

#### 11.6

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Remove processing information from Transfer screen in the Dashboard
  - [ ] The processing information will no longer appear on the Transfer screen

#### 11.7

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Remove processing information from Ingest screen in the Dashboard
  - [ ] The processing information will no longer appear on the Ingest screen

#### 11.8

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Add MCP processing configuration xml file to a transfer directory.

### 12. Add Metadata

#### 12.1

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Add and delete rights metadata through the GUI.

#### 12.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Add and delete descriptive metadata through the GUI.

#### 12.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Process a transfer with an accession number
  - [ ] number should end up in METS as a registration event outcome detail note.

### 13. Backlog

#### 13.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Send a transfer to backlog at "Job: Create SIP(s)?" And download from the backlog
  - [ ] When the processingMCP.xml is configured to send to backlog
  - [ ] And processing is COMPLETE
  - [ ] And the UUID is BACKLOG
  - [ ] And the SIP can be downloaded
  - [ ] And validated as a BAG
  - [ ] And the transfer METS contains certain information

#### 13.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Search transfer backlog - perform as many searches as you can, searching on all parameters Any File name File extension Accession number Ingest date SIP UUID
  - [ ] Searches for known items should be successful

#### 13.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Send a delete request (confirm in SS and delete)
  - [ ] Transfer should be removed from backlog screen

#### 13.4

**Severity**: n/a

**Current test coverage**: none

**External tools**: none

- [ ] Start SIP from backlog by using the widget on the Ingest tab (whole and part)
  - [ ] (This feature has been deprecated, covered by Appraisal tab functionality below)

### 14. Appraisal

#### 14.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Search Backlog
  - [ ] Searches for known items should be successful

#### 14.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Backlog panel: add tags
  - [ ] tags should be visible in backlog pane as well as in dropdown

#### 14.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Backlog panel: Deselect, collapse, expand
  - [ ] users should be able to navigate easily through the backlog pane

#### 14.4

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Analysis panel - Report -
  - [ ] make sure they’re accurate (select/deselect files in backlog pane)

#### 14.5

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Analysis panel - Visualizations
  - [ ] make sure they’re accurate (select/deselect files in backlog pane)

#### 14.6

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Analysis panel - tags
  - [ ] make sure they’re accurate (select/deselect files in backlog pane)

#### 14.7

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Examine contents
  - [ ] If using DemTransfer there should be hits in Examine Contents
  - [ ] Should be visible in Examine Contents; Credit card numbers

#### 14.8

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Preview file (need to select file from File list pane)
  - [ ] Should be able to expand file preview pane for an image if using Firefox
  - [ ] Non-previewable files (e.g. .doc files) should download for preview

#### 14.9

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] File list: Tags - delete tags
  - [ ] Tags should be removed from the backlog view as well as the drop-down.

#### 14.10

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] File list: Show path/hide path
  - [ ] Toggles path column on and off in file list

### 15. ArchivesSpace - Appraisal tab workflow

#### 15.1

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] View resources
  - [ ] Search for known resources by title or resource number

#### 15.2

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Add child record
  - [ ] Should be able to add a child record to an existing resource

#### 15.3

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Add new digital object and drag DO over
  - [ ] Click to add a new digital object; click and drag object over from backlog

#### 15.4

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Edit rights metadata

#### 15.5

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Edit metadata

#### 15.6

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Delete selected

#### 15.7

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Finalize arrangement and Create SIP
  - [ ] (it won’t appear in AS but everything else should look normal, i.e. you should be able to make an AIP)

#### 15.8

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Arrangement pane: Arrange selected items

#### 15.9

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Create SIP

#### 15.10

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Delete

#### 15.11

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Reload

### 16. Integrations: Access Systems

#### 16.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Arrange transfer from backlog: Add AtoM levels of description and upload to AtoM
  - [ ] from appraisal tab
  - [ ] Check that logical structMap has been created
  - [ ] Check that levels of description are present after upload to AtoM

#### 16.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - AtoM 2.5

#### 16.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Upload Dip - AtoM 2.5 with levels of description
  - [ ] check AtoM to ensure DIP uploaded successfully

#### 16.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - AtoM 2.5 with slug added to access system ID box
  - [ ] check AtoM to ensure DIP uploaded successfully

#### 16.5

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - Binder

#### 16.6

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - Binder with identifier added to access system ID box

#### 16.7

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - ArchivesSpace 2.5 matching GUI (regular workflow)

#### 16.8

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - ArchivesSpace 2.5 with CSV

#### 16.9

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Upload DIP - CONTENTdm
  - [ ] make sure transfer has a metadata.csv; after DIP is created check uploadedDIPs and ensure a simple.txt or compound.txt has been created and contains descriptive metadata from the csv

### 17. Archival Storage

#### 17.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Store AIP
  - [ ] AIP is stored as anticipated if the drop-down is used

#### 17.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Reject AIP
  - [ ] AIP is sent to the rejected directory if the drop-down is used AND
  - [ ] The AIP can be accessed from the rejected directory

#### 17.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Search:
  - [ ] Show files
  - [ ] Show AICs
  - [ ] Any
  - [ ] File path
  - [ ] File extension
  - [ ] AIP UUID
  - [ ] AIP name
  - [ ] Identifiers
  - [ ] Part of AIC
  - [ ] AIC identifier
  - [ ] Transfer metadata
  - [ ] Transfer metadata (other)

#### 17.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Download AIP

#### 17.5

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Make an AIC

#### 17.6

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Reingest
  - [ ] <premis:eventType>reingestion</premis:eventType> is present in METS

#### 17.7

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Delete an AIP

### 18. Preservation Planning

#### 18.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Search

#### 18.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Disable rules/commands

#### 18.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Disable tool commands - disable Siegfried; processing config for file ID should automatically be set to “None” if it was set to Siegfried before; Siegfried should not be option in tool drop-down

#### 18.4

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Change rules/commands

### 19. Access

#### 19.1

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Check links to uploaded AtoM descriptions

### 20. Administration

#### 20.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Processing config

#### 20.2

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Clear processing storage locations

#### 20.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Add AtoM/AS configs

#### 20.4

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] PREMIS agent

#### 20.5

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Change language
  - [ ] A sample of microservice tasks and menu items can be verified as correct for either language

#### 20.6

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Check version
  - [ ] Agent string is correct AND
  - [ ] Version in GUI is correct AND
  - [ ] Anything else?

### 21. Users & Permissions

#### 21.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Add users

#### 21.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a user does not have administration permissions
  - [ ] Then they should NOT have access to....

#### 21.3

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] When a user has administration permissions
  - [ ] Then they should have access to...

#### 21.4

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] When LDAP is configured

### 22. Failure Reports & Notifications

#### 22.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] view failure report in dashboard

#### 22.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] receive email with failure report

### 23. System Config Options

#### 23.1

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Indexing Disabled
  - [ ] some screens aren't visible?
  - [ ] the Index AIP microservice... doesn't run?

#### 23.2

**Severity**: Low

**Current test coverage**: none

**External tools**: none

- [ ] Task Output Disabled
  - [ ] https://www.archivematica.org/en/docs/archivematica-1.9/admin-manual/installation-setup/customization/task-config/

### 24. Storage Service

#### 24.1

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Perform a fixity check

#### 24.2

**Severity**: High

**Current test coverage**: none

**External tools**: none

- [ ] Delete a DIP

#### 24.3

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] AIP Recovery

#### 24.4

**Severity**: Medium

**Current test coverage**: none

**External tools**: none

- [ ] Storage types -- should we have a test for the main storage types? S3, NFS etc.  You could repeat all of the tests in this section for each storage type
