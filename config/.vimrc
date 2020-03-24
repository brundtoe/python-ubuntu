"ref. https://github.com/mlavin/dotfiles/blob/master/vimrc
"uddrag medtaget fra ref.

set encoding=utf-8
set fileencoding=utf-8

syntax enable
set ttyfast
set showmode
set showcmd
set title
set number
set hidden

" This is what files look like
set ffs=unix,dos,mac

" Update find path to search subdirectories
set path=$PWD/**


" Tab sanity
set expandtab
set tabstop=4
set shiftwidth=4

" Different tab/space stops"
autocmd Filetype yaml setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd Filetype html setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd Filetype css setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd Filetype scss setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd Filetype json setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd Filetype javascript setlocal tabstop=2 shiftwidth=2 softtabstop=2 expandtab
autocmd FileType make setlocal noexpandtab

" No backups
set nobackup
set nowritebackup
set nowb
set noswapfile

" Keep lots of history/undo
set undolevels=1000

" Files to ignore
" Python
set wildignore+=*.pyc,*.pyo,*/__pycache__/*
" Temp files
set wildignore+=*.swp,~*
" Archives
set wildignore+=*.zip,*.tar

" Update find path to search subdirectories
set path=$PWD/**
