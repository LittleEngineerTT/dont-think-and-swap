import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import Box from '@mui/material/Box'

import config from './config.d/config.yaml';

interface RouteCreatorInterface {
    name: string;
}

const RouteCreator: React.FC<RouteCreatorInterface> = ({name}) => {
    if (name == config.routes.example) {
        return (
            <Box sx={{
                height: "100vh",
            }}>
            </Box>
        )
    } else {
        return (
            <Box sx={{
                    height: "100vh",
                  }}>
            </Box>
        )
    }

}

const App = () => {
  let routes: string[] = [];
  for (let key in config.routes) {
      routes.push(config.routes[key]);
  }

  return (
    <BrowserRouter>
      <Routes>
          {routes.map((route) => (
                <Route key={route} path={route} element={<RouteCreator name={route} />}/>
              ))
          }
          <Route path="/" element={<Navigate to={config.routes.devices} />} />
        <Route path="*" element={<Navigate to="/" replace={true} />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;