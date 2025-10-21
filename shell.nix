{ pkgs ? import <nixpkgs> {}}:

pkgs.mkShell {
    buildInputs = with pkgs; [
      (python3.withPackages(ps: with ps; [
            ipython
            jupyter
            numpy
            pandas
            python-lsp-server
            streamlit
            plotly
            matplotlib
      ]))

      opencv
      poppler-utils
      ruff
    ];

    shellHook = ''
      # python3 -m venv venv && source venv/bin/activate
      echo "Environmnent up !"
      exec zsh
    '';
}
