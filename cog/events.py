import pygame

class Events:
    """Handles pygame and custom controller events.

    Keyword arguments:
    event_type -- If a type or sequence of types is given,
                  only those messages will be removed from the queue.
    """

    def __init__(self, event_type=None):
        """Constructor of Events class.

        Keyword arguments:
        event_type -- If a type or sequence of types is given, only
                      those messages will be removed from the queue.
        """

        self.event_type = event_type

        self.events = []

    def __iter__(self):
        """Iterator of Events class."""

        self.update()

        return EventIterator(self.events)

    def update(self):
        """Updates the event list."""

        self.events = []

        for event in pygame.event.get(self.event_type):
            event_converted = Event(event, "host")
            self.events.append(event_converted)


class Event:
    """Represents an event.

    Keyword arguments:
    event -- Either pygame event or custom controller event.
    level -- If pygame event, 'host';
             if custom controller event, 'controller'.
    """

    def __init__(self, event, level):
        """Constructor of Event class.

        Keyword arguments:
        event -- Either pygame event or custom controller event.
        level -- If pygame event, 'host';
                 if custom controller event, 'controller'.
        """
        if level == "host":
            self.__dict__.update(event.__dict__)
            self.type = event.type

        self.level = level

    def __eq__(self, other):
        """Equality of Event class."""

        if isinstance(other, type(self.type)):
            return self.type == other
        return False


class EventIterator:
    """Iterator for events.

    Keyword arguments:
    events -- List of events.
    """

    def __init__(self, events):
        """Constructor of EventIterator class.

        Keyword arguments:
        events -- List of events.
        """
        self.index = 0
        self.events = events

    def __next__(self):
        """Next of EventIterator class."""

        if self.index >= len(self.events):
            raise StopIteration

        temp_index = self.index
        self.index += 1

        return self.events[temp_index]
