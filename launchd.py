on Launch(){
  function imports(){
    import time
    import os
    import mail
    import terminal
    import kernel
    import manjaro
    import kotlin
  };
  call imports();
  call os();
  if os == win(){
    terminal cd %appdata%/kotlin/releases/main.jar %appdata%/launchd/kotlin/
  };
  if os == mac(){
    terminal cd ~/Library/Application%20Support/kotlin/releases/main.bundle ~/Library/Application%20Support/launchd/kotlin/
  };
  if os == linux(){
    terminal cd ~/Library/Application%20Support/kotlin/releases/main.bundle ~/Library/Application%20Support/launchd/kotlin/
  };
};

@import /main/main.py
