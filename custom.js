// we want strict javascript that fails
// on ambiguous syntax
"using strict";

// do not use notebook loaded  event as it is re-triggerd on
// revert to checkpoint but this allow extension to be loaded
// late enough to work.

$([IPython.events]).on('app_initialized.NotebookApp', function(){

IPython.load_extensions('autosavetime');
IPython.load_extensions('calico-spell-check');
//IPython.load_extensions("celltags");
IPython.load_extensions('comment-uncomment');
IPython.load_extensions('hide_input');
IPython.load_extensions('hide_input_all');
IPython.load_extensions('linenumbers');
IPython.load_extensions('navigation-hotkeys');
IPython.load_extensions('nbconvert_button');
IPython.load_extensions('noscroll');
IPython.load_extensions('printviewmenu_button');
IPython.load_extensions('read-only');
IPython.load_extensions('shift-tab');
IPython.load_extensions('split-combine');
IPython.load_extensions('toc');
IPython.load_extensions('toggle_all_line_number');
});
