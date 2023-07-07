# BicorneBot
> A Telegram bot for administrating groups.

## About
BicorneBot is a simple solution for small groups wanting to keep their audience 
safe from unwanted content. The bot will provide a network of chat rooms in 
which penalties are automatically applied to all chat rooms on the network. 

## Features
- [ ] [Kick users](#kick-users)
- [ ] [Ban users](#ban-users)
- [ ] [Mute users](#mute-users)
  - [ ] Permanent mute
  - [ ] Temporary mute
  - [ ] Unmute users
- [ ] [Warn users](#warn-users)
- [ ] [User management](#user-management)
  - [ ] `Ignore User`
  - [ ] `Unignore User`
  - [ ] `Ignorelist`
- [ ] [CAPTCHA system](#captcha-system)
  - [ ] Text CAPTCHA
- [ ] [Report system](#report-system)
  - [ ] `Mute`
  - [ ] `Kick`
  - [ ] `Ban`
  - [ ] `Warn`
  - [ ] `Mute Reporter`
  - [ ] `Ignore Reporter`

### Kick users
Kicks a user from the chat room. 
The user can rejoin the chat room.

### Ban users
Bans a user from the chat room.
The user cannot rejoin the chat room.

### Mute users
Mutes a user in the chat room.
The user cannot send messages in the chat room.

#### Permanent mute
Mutes a user in the chat room permanently.
The user cannot send messages in the chat room.

#### Temporary mute
Mutes a user in the chat room for a specified amount of time.
The user cannot send messages in the chat room.

#### Unmute users
Unmutes a user in the chat room.
The user can send messages in the chat room.

### Warn users
Warns a user in the chat room.
The user is notified of the warning.

### User management
#### `Ignore User`
Ignores a user. His messages will not be processed by the bot.

#### `Unignore User`
Unignores a user. His messages will be processed by the bot.

#### `Ignorelist`
Lists all ignored users.

### CAPTCHA system
#### Text CAPTCHA
Sends a CAPTCHA to the user. The user must solve the CAPTCHA to send messages
in the chat room.

### Report system
#### `Mute Reporter`
If a person makes a report for no reason, he should be punished. 
This command mutes the reporter for a specified amount of time.

#### `Ignore Reporter`
If a person makes a report for no reason, he should be punished.
This command ignores the reporter.