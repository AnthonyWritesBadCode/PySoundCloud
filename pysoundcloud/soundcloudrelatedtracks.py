from pysoundcloud.soundcloudtrack import SoundCloudTrack


class SoundCloudRelatedTracks:
    tracks: list = None
    next_href: str = ""
    query_urn: str = ""
    variant: str = ""

    """
    :var tracks: The related tracks
    :var next_href: The URL for the next page of results
    :var query_urn: The API resource URL for this query
    :var variant:
    """

    def __init__(self, data: dict, client_id: str = None):
        """
        :param data: The json dict from the response
        :param client_id: The ID of the client
        """
        self.index = 0
        self.tracks = list()
        self.next_href = data["next_href"]
        self.query_urn = data["query_urn"]
        self.variant = data["variant"]
        for track in data["collection"]:
            self.tracks.append(SoundCloudTrack(track, client_id))

    def __iter__(self):
        return self

    def __next__(self) -> SoundCloudTrack:
        try:
            value = self.tracks[self.index]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration
