import { ThemeProvider, CssBaseline } from "@mui/material";
import { theme } from "./styles/theme";
import { Home } from "./pages/Home/Home";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Home />
    </ThemeProvider>
  );
}

export default App;
