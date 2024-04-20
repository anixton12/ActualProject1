class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television instance."""
        self._status = False  # TV is initially off
        self._muted = False   # TV is initially unmuted
        self._volume = Television.MIN_VOLUME  # Start at minimum volume
        self._channel = Television.MIN_CHANNEL  # Start at minimum channel

    def power(self):
        """Toggle the power status of the TV (on/off)."""
        self._status = not self._status

    def mute(self):
        """Toggle the muted status of the TV, only if the TV is on."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Increase the channel, wrapping around to MIN_CHANNEL at MAX_CHANNEL."""
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the channel, wrapping around to MAX_CHANNEL at MIN_CHANNEL."""
        if self._status:
            self._channel = (self._channel - 1) if self._channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self):
        """Increase the volume by one, stopping at MAX_VOLUME. Unmute if muted."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        """Decrease the volume by one, stopping at MIN_VOLUME. Unmute if muted."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f"Power={'True' if self._status else 'False'}, Channel={self._channel}, Volume={self._volume if not self._muted else '0'}"

# Example usage and testing setup
if __name__ == "__main__":
    tv = Television()
    print(tv)  # Should print the initial status, channel and volume.
