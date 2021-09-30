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
    terminal cd %appdata%/kotlin/releases/1.23.1.jar %appdata%/launchd/kotlin
  };
