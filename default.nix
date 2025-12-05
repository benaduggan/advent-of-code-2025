{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2025-12-04";
      url = "https://github.com/jpetrucciani/nix/archive/c12d8df98f37d788e47a305901566bad77ca69d6.tar.gz";
      sha256 = "0ffy7d0dhnw4j0zqwf4xgp77wbzswrdvi74y95paw60cvqi8qjvq";
    })
    { }
}:
let
  name = "advent-of-code-2025";

  tools = with pkgs; {
    cli = [
      jfmt
      nixup
    ];
    python = [
      ruff
      (python313.withPackages (p: with p; [
        black
      ]))
    ];
    scripts = pkgs.lib.attrsets.attrValues scripts;
  };

  scripts = with pkgs; { };
  paths = pkgs.lib.flatten [ (builtins.attrValues tools) ];
  env = pkgs.buildEnv {
    inherit name paths; buildInputs = paths;
  };
in
(env.overrideAttrs (_: {
  inherit name;
  NIXUP = "0.0.10";
})) // { inherit scripts; }
