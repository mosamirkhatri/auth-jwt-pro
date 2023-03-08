// Library
import { BrowserRouter } from "react-router-dom";
import { MantineProvider } from "@mantine/core";
import { Global } from "@mantine/core";
// Component - Router
import AppRouter from "./router/AppRouter";
// AxiosDefaults
import { setAxiosDefaults } from "./utils/setAxiosDefaults";

setAxiosDefaults();

function MyGlobalStyles() {
  return (
    <Global
      styles={(theme) => ({
        "*, *::before, *::after": {
          margin: 0,
          padding: 0,
          boxSizing: "border-box",
          fontFamily: `"Fira Sans", Inter, sans-serif`,
        },
      })}
    />
  );
}
function App() {
  return (
    <BrowserRouter>
      <MantineProvider>
        <MyGlobalStyles />
        <AppRouter />
      </MantineProvider>
    </BrowserRouter>
  );
}

export default App;
