class Signals:
    def __init__(self):
        self.list_signal = [{}]

    def signal(self, send=None, reseve=None, list_num: int = 0):
        """
        >>> ex_code (signal(); --code--; clear())
        Args:
            send (str, optional): send_signal. Defaults to None.
                -> if optional is given save
            reseve (str, optional): reseve_signal. Defaults to None.
                -> if optional is given save and compare with send
            list_num (int, optional): index of list. Defaults to 0.
                -> save_listpos

        Returns:
            bool: if send and reseve -> True
            ⚠️ WARNING: This will reset the signal values.

        Examples:
            This is an example of how to use the function:

            >>> signal(send="attack")
            >>> signal(reseve="attack") -> True


        """

        while len(self.list_signal) <= list_num:
            self.list_signal.append({})

        if send is not None:
            self.list_signal[list_num]["send"] = send
        if reseve is not None:
            self.list_signal[list_num]["reseve"] = reseve

        send_val = self.list_signal[list_num].get("send")
        reseve_val = self.list_signal[list_num].get("reseve")

        if send_val is not None and reseve_val is not None:
            return send_val == reseve_val

        return False

    def clear(self, list_num: int = 0):
        """Clear of the list_num's valuable."""
        while len(self.list_signal) <= list_num:
            self.list_signal.append({})  # 확장 필요시 대응

        self.list_signal[list_num].pop("send", None)
        self.list_signal[list_num].pop("reseve", None)