SetCapsLockState, AlwaysOff

; [CapsLock] + [D] - print current date
CapsLock & d::
  FormatTime, CurrentDateTime,, yyyy-MM-dd
  SendInput %CurrentDateTime%
  return
Return

; [CapsLock] + [g] - opening google chrome
CapsLock & g::
  Run, C:\Program Files\Google\Chrome\Application\chrome.exe
  return
Return

; TODO [CapsLock] + [d] + [s] - daily schedule related Software and Websites

; [CapsLock] + [b] - opening battlenet
CapsLock & b::
  Run, F:\Programme\Games\Battle.net\Battle.net Launcher.exe
  return
Return

; Change volume
CapsLock & WheelUp::Volume_Up
CapsLock & WheelDown::Volume_Down

; Empty trash
#Del::FileRecycleEmpty ; win + del
return

; Google Search highlighted text
^+c::
{
 Send, ^c
 Sleep 50
 Run, http://www.google.com/search?q=%clipboard%
 Return
}

