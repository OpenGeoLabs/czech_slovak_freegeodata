class ShiftGrid:
    """
    Represents shift grid needed to enable certain transformations.
    """

    def __init__(self, gridKey, gridFileUrl, gridFileName):
        """
        gridKey - unique grid key
        gridFileUrl - URL to download grid
        gridFileName - grid filename
        """

        self.key = gridKey
        self.fileUrl = gridFileUrl
        self.fileName = gridFileName
