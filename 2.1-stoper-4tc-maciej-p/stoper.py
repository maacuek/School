"""
Stoper – a desktop stopwatch application.
Built with Python and tkinter (no HTML).
"""

import tkinter as tk
import time


class Stoper(tk.Tk):
    """Main stopwatch application window."""

    # ── colour palette ──────────────────────────────────────────────
    BG           = "#1e1e2e"
    FG_TIME      = "#cdd6f4"
    FG_MS        = "#6c7086"
    BTN_START_BG = "#a6e3a1"
    BTN_START_FG = "#1e1e2e"
    BTN_STOP_BG  = "#f38ba8"
    BTN_STOP_FG  = "#1e1e2e"
    BTN_RESET_BG = "#89b4fa"
    BTN_RESET_FG = "#1e1e2e"
    ACCENT       = "#cba6f7"

    def __init__(self) -> None:
        super().__init__()

        self.title("Stoper")
        self.configure(bg=self.BG)
        self.resizable(False, False)
        self.geometry("420x320")

        # ── state ────────────────────────────────────────────────────
        self._running = False
        self._start_time: float = 0.0
        self._elapsed: float = 0.0          # seconds accumulated before last stop

        # ── title label ──────────────────────────────────────────────
        tk.Label(
            self,
            text="⏱  STOPER",
            font=("Segoe UI", 16, "bold"),
            fg=self.ACCENT,
            bg=self.BG,
        ).pack(pady=(20, 5))

        # ── time display ─────────────────────────────────────────────
        self._time_var = tk.StringVar(value="00:00:00")
        tk.Label(
            self,
            textvariable=self._time_var,
            font=("Consolas", 48, "bold"),
            fg=self.FG_TIME,
            bg=self.BG,
        ).pack(pady=(5, 0))

        self._ms_var = tk.StringVar(value=".000")
        tk.Label(
            self,
            textvariable=self._ms_var,
            font=("Consolas", 22),
            fg=self.FG_MS,
            bg=self.BG,
        ).pack(pady=(0, 20))

        # ── buttons ──────────────────────────────────────────────────
        btn_frame = tk.Frame(self, bg=self.BG)
        btn_frame.pack()

        btn_style = dict(
            font=("Segoe UI", 13, "bold"),
            width=8,
            relief="flat",
            bd=0,
            cursor="hand2",
            activeforeground="#1e1e2e",
        )

        self.btn_start = tk.Button(
            btn_frame,
            text="▶  Start",
            bg=self.BTN_START_BG,
            fg=self.BTN_START_FG,
            activebackground="#77d4a0",
            command=self._start,
            **btn_style,
        )
        self.btn_start.grid(row=0, column=0, padx=8)

        self.btn_stop = tk.Button(
            btn_frame,
            text="■  Stop",
            bg=self.BTN_STOP_BG,
            fg=self.BTN_STOP_FG,
            activebackground="#e06080",
            command=self._stop,
            state="disabled",
            **btn_style,
        )
        self.btn_stop.grid(row=0, column=1, padx=8)

        self.btn_reset = tk.Button(
            btn_frame,
            text="↺  Reset",
            bg=self.BTN_RESET_BG,
            fg=self.BTN_RESET_FG,
            activebackground="#6a9ae8",
            command=self._reset,
            **btn_style,
        )
        self.btn_reset.grid(row=0, column=2, padx=8)

        # ── kick off the display loop ────────────────────────────────
        self._tick()

    # ── actions ──────────────────────────────────────────────────────

    def _start(self) -> None:
        """Start (or resume) the stopwatch."""
        if not self._running:
            self._running = True
            self._start_time = time.perf_counter()
            self.btn_start.configure(state="disabled")
            self.btn_stop.configure(state="normal")

    def _stop(self) -> None:
        """Pause the stopwatch, preserving elapsed time."""
        if self._running:
            self._elapsed += time.perf_counter() - self._start_time
            self._running = False
            self.btn_start.configure(state="normal")
            self.btn_stop.configure(state="disabled")

    def _reset(self) -> None:
        """Reset everything back to zero."""
        self._running = False
        self._elapsed = 0.0
        self._start_time = 0.0
        self._update_display(0.0)
        self.btn_start.configure(state="normal")
        self.btn_stop.configure(state="disabled")

    # ── display ──────────────────────────────────────────────────────

    def _tick(self) -> None:
        """Refresh the time display ~every 33 ms (~30 fps)."""
        if self._running:
            total = self._elapsed + (time.perf_counter() - self._start_time)
            self._update_display(total)
        self.after(33, self._tick)

    def _update_display(self, total_seconds: float) -> None:
        """Format and show the elapsed time."""
        hrs, rem = divmod(int(total_seconds), 3600)
        mins, secs = divmod(rem, 60)
        ms = int((total_seconds - int(total_seconds)) * 1000)
        self._time_var.set(f"{hrs:02d}:{mins:02d}:{secs:02d}")
        self._ms_var.set(f".{ms:03d}")


# ── entry point ──────────────────────────────────────────────────────
if __name__ == "__main__":
    app = Stoper()
    app.mainloop()
