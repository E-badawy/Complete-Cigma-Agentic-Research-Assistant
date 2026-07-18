import { createContext, useContext, useState } from "react";

const ResearchContext = createContext();

export function ResearchProvider({ children }) {

    const [report, setReport] = useState(null);

    return (

        <ResearchContext.Provider
            value={{
                report,
                setReport,
            }}
        >

            {children}

        </ResearchContext.Provider>

    );

}

export function useResearch() {

    return useContext(ResearchContext);

}