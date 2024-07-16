import unittest
from agenda import Agenda


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("Meeting", "2024-07-20", "Team meeting con Simone")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].title, "Meeting")

    def test_remove_event(self):
        self.agenda.add_event("Meeting", "2024-07-21", "Team meeting con Elisabetta")
        self.agenda.remove_event("Meeting")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 0)

    def test_list_events(self):
        self.agenda.add_event("Meeting", "2024-07-20", "Team meeting con Simone")
        self.agenda.add_event("Conference", "2024-08-15", "Tech conference al Polimi")
        events = self.agenda.list_events()
        self.assertEqual(len(events), 2)


if __name__ == "__main__":
    unittest.main()
