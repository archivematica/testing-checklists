---
name: Testing checklist template
about: Use this template to create an issue for regression testing

---

## Transfer

### Transfer types
- [ ] **Standard**: process a Standard transfer using SampleTransfers/Images. Validate the METS. The resulting AIP should store without error.
- [ ] **Unzipped Bag**: process an Unzipped Bag transfer using SampleTransfers/BagTransfer. The bag should verify during “Job: Verify bag, and restructure for compliance”. Validate the METS. The resulting AIP should store without error.
- [ ] **Zipped Bag**: process a Zipped Bag transfer using SampleTransfer/BagTransfer.zip. The bag should verify during “Job: Verify bag, and restructure for compliance”. Validate the METS. The resulting AIP should store without error.
- [ ] **DSpace**: process a DSpace transfer using SampleTransfer/DSpaceExport (or one of the zips contained inside). All DSpace-specific microservices should succeed. Validate the METS. The resulting AIP should store without error.
- [ ] **Disk Image**: process a Disk Image transfer using SampleTransfer/ISODiskImage. Before starting the transfer, add disk image metadata. Validate the METS. Make sure that the disk image metadata ends up in the AIP METS.
- [ ] **Dataverse**: process the three Dataverse transfers separately (SampleTransfers/Dataverse/AStudyOfMyAfternoonDrinks, SampleTransfers/Dataverse/NDSAStaffingReport, SampleTransfers/Dataverse/XRayScansOfPolyodonSpathula). Make sure that Archivematica is NOT set to delete packages after extraction. “Job: parse external files” should succeed. Validate the METS. Download the AIP and look at the Dataverse METS (buried somewhere in objects/transfer) - it should contain DDI metadata.

### Transfer directory variants

- [ ] **Metadata (rights and descriptive) and submission documentation**:
  - [ ] Process a transfer using *SampleTransfer/DemoTransfer*. The AIP METS should contain metadata from the description and rights CSVs. Submission documentation should also be preserved and listed in the AIP METS with the correct file group use (it should be `fileGrp USE="submissionDocumentation"`)
  - [ ] Process a transfer using *SampleTransfer/CSVmultiLevel*. The AIP METS should contain multi-level descriptive metadata from the CSV.
- [ ] **Existing checksums**: If *SampleTransfer/DemoTransfer* didn’t fail at “Job: Verify metadata directory checksums” when you transferred it above, check this off!
  - [ ] Check to make sure fixity will fail if something’s wrong by transferring *TestTransfers/fixityCheckShouldFail*
- [ ] **Preservation and access derivatives**: Change your processing config: set “Normalization” to None and “Approve normalization” to None. Process a transfer using *TestTransfers/ManualNormalization*. At Normalization, choose “Normalize for preservation and access”. Originals should be .dat, .TGA, and .GIF; preservation copies should be .prk, .tif, and .tif; access copies should be .bmp, .jpg, and .jpg.
- [ ] **Access derivatives**: Change your processing config: set “Normalization” to None and “Approve normalization” to None. Process a transfer using *SampleTransfers/transfer-with-access-copies*. “Job: Normalize” should only give three options - choose “Normalize for preservation”. Originals should be .png, preservation copies should be as per rule, access copies should be .bmps
- [ ] **Service files**: Change your processing config: set “Normalization” to None and “Approve normalization” to None. Run service-files transfer and choose “Normalize service files for access”. “Job Normalize service files for access” should run and the task output should show that the service files were used to create access copies.
