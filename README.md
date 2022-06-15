My django project skeleton for quick start.

Place `.env` in `./server/` : 
```
DEBUG=1
SECRET_KEY=django-insecure-idk4x5h(v8a0j*rh3b7kr^kwuo$t7yn3!85$*8fce3d-f0^(8u
```

My basic Sublime-Text configuration:
```JSON
{
	"folders":
	[
		{
			"path": "server/core",
			"folder_exclude_patterns": ["__pycache__","static"],
			"file_exclude_patterns": [".gitkeep"]
		},
		{
			"path": "server/apps",
			"folder_exclude_patterns": ["__pycache__","migrations","sandbox",],
			"file_exclude_patterns": ["__init__.py",".gitkeep",]
		},
		{
			"path": "server/assets/templates",
			"file_exclude_patterns": [".gitkeep"]
		},
		{
			"path": "server/core/static",
			"file_exclude_patterns": [".gitkeep"],
		},
		{
			"path": "server/apps/sandbox",
			"folder_exclude_patterns": ["__pycache__","migrations",],
			"file_exclude_patterns": [".gitkeep"],
		}
	]
}
```