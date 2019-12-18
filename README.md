Python notes to cover whatever is needed to become python expert

Organization
1. Basics
2. Advanced
3. Libraries
4. Networking/URLs/Server stuff
5. Example tools - also see python-tools

Note all python scripts should follow these rules:
1) No #!/...path/to/python - Need to run both Python 2 and 3
2) Data files for ALL parts must be kept in data directory only
3) ALL scripts must be run for both V2 and V3. Major differences
   can be in separate files. 
4) All test files for each section must go into testdir# dirs
5) All print statements must be enclosed with ()
6) All functions that create/delete something should do the opposite
    ie: if you delete a file, re-create it after deletion...
7) Catch ALL errors where it makes sense. Always crash gracefully.

