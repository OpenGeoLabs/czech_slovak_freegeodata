class ShiftGridList(list):
    """
    Represents list of shift grids and allows to preform some usefull queries and oprations over them.
    """

    def getGridsByKeys(self, keys):
        """
        Returns grids according to specified keys filter. Keys may be single key string, or list/tuple of key stings.
        """

        assert isinstance(keys, (tuple, list, str))

        outGrids = ShiftGridList()

        for grid in self:

            if isinstance(keys, str):
                if grid.key == keys:
                    outGrids.append(grid)
                    return outGrids

            else:
                if grid.key in keys:
                    outGrids.append(grid)

        return outGrids

    def downloadAll(self):
        """
        Downloads all contained shift grids.
        """

        for grid in self:
            grid.download()
