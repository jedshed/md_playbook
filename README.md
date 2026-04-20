# md_playbook

## Description:
Gets latest london playbook newsletter url
Creates md file inc yaml frontmatter and
Moves md file to Obsidian Vault on network share

### 0.2.0
- filename name version suffix removed for git compatibility
- toml project name - version siffix removed
- toml description added
- created .gitignore and populated with minimil ignores
cd


### 0.1.6 - 0.1.9
- project version upped to 0.2.0 as pushing to github

### 0.1.5
- meta_data_publish created as oldest of meta_date or meta_filedate
- helper_functions folder added
- helper_update_remote_line to make remote line replace clearer
- convert function renamed to create_latest_md_content
  for clarification and consistency
- 'processes' functions created to seperate REGEX & Replacefor clarity
  and updating
  - process_md_title
  - process_md_header
  - process_md_conrent
- do_display args simplified where possible for reusability
- Tidy up of extract_metadata display stdout

### 0.1.4
- config project_name and project_version now pulls from toml file 
- config url changed to base_url
- f-string padding added to print statement - width set in config
- get_url_latest modified adding curl-cffi to impersonte 'human' browser
  web page had started bot-blocking