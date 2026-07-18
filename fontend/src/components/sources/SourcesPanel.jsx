import PaperCard from "./PaperCard";

function SourcesPanel({
    localSources = [],
    webSources = [],
    references = [],
}) {

    console.log("SourcesPanel:", {
        localSources,
        webSources,
        references,
    });

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-2xl font-bold text-slate-800 mb-8">
                Research Sources
            </h2>

            {/* ---------------- Local Sources ---------------- */}

            <section className="mb-10">

                <h3 className="text-lg font-semibold text-blue-700 mb-4">
                    📚 Local Library Sources
                </h3>

                {
                    localSources.length > 0 ? (

                        <div className="space-y-3">

                            {localSources.map((source, index) => (

                                <div
                                    key={`${source.filename}-${index}`}
                                    className="border rounded-xl p-4 bg-blue-50"
                                >

                                    <p className="font-semibold text-slate-800">
                                        {source.filename}
                                    </p>

                                    <p className="text-sm text-gray-600 mt-1">
                                        Page {source.page + 1}
                                    </p>

                                </div>

                            ))}

                        </div>

                    ) : (

                        <p className="text-gray-500 italic">
                            No local library sources were used.
                        </p>

                    )
                }

            </section>

            {/* ---------------- References ---------------- */}

            <section className="mb-10">

                <h3 className="text-lg font-semibold text-green-700 mb-4">
                    📖 References
                </h3>

                {
                    references.length > 0 ? (

                        <ol className="list-decimal pl-6 space-y-3">

                            {references.map((reference, index) => (

                                <li
                                    key={index}
                                    className="text-gray-700 leading-7"
                                >
                                    {reference}
                                </li>

                            ))}

                        </ol>

                    ) : (

                        <p className="text-gray-500 italic">
                            No references generated.
                        </p>

                    )
                }

            </section>

            {/* ---------------- Latest Papers ---------------- */}

            <section>

                <h3 className="text-lg font-semibold text-purple-700 mb-4">
                    🧬 Latest Scientific Papers
                </h3>

                {
                    webSources.length > 0 ? (

                        <div className="space-y-6">

                            {webSources.map((paper, index) => (

                                <PaperCard
                                    key={paper.doi || paper.title || index}
                                    paper={paper}
                                />

                            ))}

                        </div>

                    ) : (

                        <p className="text-gray-500 italic">
                            No web papers were retrieved.
                        </p>

                    )
                }

            </section>

        </div>

    );

}

export default SourcesPanel;