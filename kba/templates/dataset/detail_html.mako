<%inherit file="../home_comp.mako"/>
<div class="row-fluid">
    <h2>Welcome to the KBA project</h2>

    <p class="lead">
        The Kalahari Basin area: a 'Sprachbund' on the verge of extinction.
    </p>
    <p>
        The Kalahari Basin area project (KBA) is a group of linguists and social
        and
        molecular anthropologists working together on questions regarding the
        population history of non-Bantu-speaking peoples in southern Africa,
        otherwise known as <a href="TODO">'Khoisan'</a>. Although Khoisan is
        regarded by some as a single language family, the KBA will investigate
        the
        hypothesis that the various language families in this area share traits
        due
        to extensive contact.

        The languages and culture of the people in the Kalahari Basin are
        rapidly dying out, thus the project additionally aims to conduct as much
        linguistic and anthropological documentation as possible before it is
        too
        late. The KBA project is made up of <a href="TODO">six project teams</a>
        of
        scientists based at six different institutions and is funded by the
        <a href="TODO">European Science Foundation</a> and various other
        country-specific funding bodies.
    </p>
</div>
## <%def name="sidebar()">
##     <div class="well">
##         <h3>Sidebar</h3>
##         <p>
##             Content
##         </p>
##     </div>
## </%def>

<div class="row-fluid">
    <div class="span4 well well-small">
        <h3>How to cite:</h3>
        <p>
            TODO Cite information.
        </p>
    </div>
    <div class="span4" style="padding: 20px; text-align: center;">
        <img width="200" height="200"
             src="${request.static_url('kba:static/kba_logo.gif')}"
             class="image"/>
    </div>
    <div class="span4">
        <table class="table table-responsive">
            <tbody>
                ##             <tr>
                ##                 <th>
                ##                     <a href="${request.route_url('languages')}">Wordlists</a>
                ##                 </th>
                ##                 <td class="right">${wordlists}</td>
                ##             </tr>
                ##             <tr>
                ##                 <th>Synsets</th>
                ##                 <td class="right">${synsets}</td>
                ##             </tr>

            <tr>
                <th>Words</th>
                <td class="right">${words}</td>
            </tr>
                ##             <tr>
                ##                 <th>Distinct Ethnologue families</th>
                ##                 <td class="right">${ethnologue_families}</td>
                ##             </tr>
                ##             <tr>
                ##                 <th>
                ##                     Distinct ${h.external_link('http://glottolog.org/glottolog/family', label='Glottolog families')}
                ##                 </th>
                ##                 <td class="right">${glottolog_families}</td>
                ##             </tr>

            <tr>
                <th>Distinct ISO 639-3 languages</th>
                <td class="right">${iso_langs}</td>
            </tr>
                ##             <tr>
                ##                 <th>
                ##                     <a href="${request.route_url('contribute')}">
                ##                         Missing ISO 639-3 languages (from Ethnologue 17)
                ##                     </a>
                ##                 </th>
                ##                 <td class="right">${missing_iso}</td>
                ##             </tr>
            </tbody>
        </table>
    </div>
</div>