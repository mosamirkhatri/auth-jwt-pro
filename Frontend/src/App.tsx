// Library
import { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { MantineProvider, LoadingOverlay } from "@mantine/core";
// Global Styles
import GlobalStyles from "./components/shared/GlobalStyles";
// Component - Router
import AppRouter from "./router/AppRouter";
// AxiosDefaults
import { setAxiosDefaults } from "./utils/setAxiosDefaults";
// Store
import { useAuthStore } from "./store/authStore";

setAxiosDefaults();

function App() {
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const { handleGetLoggedInUser } = useAuthStore();

  useEffect(() => {
    (async () => {
      await handleGetLoggedInUser();
      setIsLoading(false);
    })();
  }, [handleGetLoggedInUser]);

  return isLoading ? (
    <LoadingOverlay visible={isLoading} overlayBlur={2} />
  ) : (
    <BrowserRouter>
      <MantineProvider>
        <GlobalStyles />
        <AppRouter />
      </MantineProvider>
    </BrowserRouter>
  );
}

export default App;
