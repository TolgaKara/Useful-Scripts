SetCapsLockState, AlwaysOff

; [CapsLock] + [D] - print current date
CapsLock & d::
  Run, https://www.linkedin.com/mynetwork/
  Run, https://www.linkedin.com/in/tolgakara/
  Run, https://github.com/TolgaKara?tab=repositories

  Run,  https://www.codewars.com/kata/search/my-languages?q=&&xids=completed&beta=false&order_by=total_completed

  Run, https://trello.com/b/5uBNznJB/written-application
  Run, https://trello.com/b/DbJnQPkX/kohovio

  ; Run, chrome://newtab
  Run, C:\Users\Tolga Kara\AppData\Local\Programs\Notion\Notion.exe

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

